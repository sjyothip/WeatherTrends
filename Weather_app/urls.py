from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='test'),

    path('index', views.multi, name='multi'),

    ]

