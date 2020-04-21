from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('abc/', views.abc, name='abc'),
    url(r'^abc/mulUuid/', views.mulUuid, name='mulUuid'),
]