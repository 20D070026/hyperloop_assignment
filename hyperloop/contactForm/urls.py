from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.form_view),
    path('submitted', views.form_data_view),
]
