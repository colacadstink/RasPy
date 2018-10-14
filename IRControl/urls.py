from django.urls import path

from . import views

urlpatterns = [
    path('', views.ir_command),
]