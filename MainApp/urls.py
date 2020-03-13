from django.conf.urls import url, include
from MainApp import views

urlpatterns = [
    url('^$', views.index, name='index')
]
