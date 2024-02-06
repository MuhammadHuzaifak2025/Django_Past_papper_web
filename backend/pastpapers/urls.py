from django.contrib import admin
from django.urls import path, re_path
from pastpapers import views

urlpatterns = [
   path("api/subjects/<str:subject_code>/", views.index, name="Index"),
]
