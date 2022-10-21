from django.urls import path
from .import views
urlpatterns=[
    path('',views.ResumeUploadView,name='home')
]