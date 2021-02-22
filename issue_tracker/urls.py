from django.urls import path

from . import views

app_name = 'issue_tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:ticket_id>/', views.ticket_comment, name="ticket_comment"),
    path('comments/<int:ticket_id>/', views.add_ticket_comment, name="add_ticket_comment"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
]
