from django.shortcuts import render,redirect

# Create your views here.
from .models import Log
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def index(request):
    # Render the HTML template index.html with the data in the context variable
    # return render(
    #     request,
    #     'index.html',
    #     context={},
    # )
    log_list = Log.objects.all()
    return render(request, "logbook/log_list.html", {'log_list':log_list})

@login_required
def logs(request):
    log_list = Log.objects.all()

    log = request.GET.get('page', 1)

    paginator = Paginator(log_list, 2)
    try:
        logs = paginator.page(log)
    except PageNotAnInteger:
        logs = paginator.page(1)
    except EmptyPage:
        logs = paginator.page(paginator.num_pages)


    return render(request, "logbook/log_list.html", {'log_list':log_list})

@login_required
def delete(request, id):
    log = Log.objects.get(pk = id)
    log.delete()
    return redirect('index')

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime


@login_required
def edit(request, id):
    log = get_object_or_404(Log, id=id)
    if request.method == "POST":
        form = AddNewLog(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddNewLog()
    return render(request, 'logbook/add_new_log.html', {'form': form, 'Log':Log})

from .forms import LogForm

def log_new(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.email = request.user.username
            log.save()
            return redirect('logs')
    else:
        form = LogForm()
    return render(request, 'logbook/log_edit.html', {'form': form})


def log_edit(request, id):
    log = get_object_or_404(Log, id=id)
    if request.method == "POST":
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.email = request.user.username
            log.save()
            return redirect('logs')
    else:
        form = LogForm()
    return render(request, 'logbook/log_edit.html', {'form': form})

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'logbook/signup.html', {'form': form})
