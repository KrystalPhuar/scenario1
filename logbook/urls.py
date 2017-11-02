from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^logs/add/$', views.add_new_log, name='addNewLog'),
]
