from django.conf.urls import url

from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), #first page -- index
    url(r'^accountsetting/$', views.AccSetting, name='accountsetting'), #account setting -- access from index
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), #detail page -- access from index
    url(r'^(?P<account_id>[0-9]+)/addlist/$', views.addlist, name='addlist'),
]