from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog', views.blog),
    path('candidate', views.candidate),
    path('contact', views.contact),
    path('elements', views.elements),
    path('job_details', views.job_details),
    path('jobs', views.jobs),
    path('singleblog', views.singleblog),
    path('tasks', views.tasks),
    path('create', views.create)
]
