"""logbook39 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from logbook.views import logs
from logbook import views
from logbook import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logbook/', include('logbook.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logbook/logs/$', views.logs , name = 'logs'),
    url(r'^logbook/delete/(?P<id>[\d]+)$', views.delete , name = 'delete'),
    # url(r'^logbook/edit/(?P<id>[\d]+)$', views.edit , name = 'edit'),
    url(r'^logbook/add/$', views.log_new, name='log_new'),
    url(r'^logbook/edit/(?P<id>\d+)/edit/$', views.log_edit, name='log_edit'),
    url(r'^logbook/signup', core_views.signup, name='signup'),
    # url(r'^log/add/$', views.add_new_log, name='add-new-log'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
url('accounts/login/', auth_views.LoginView.as_view()),
