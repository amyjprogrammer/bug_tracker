from django.urls import path

from . import views

app_name = 'issue_tracker'

urlpatterns = [
    path('', views.home, name='home'),
]
