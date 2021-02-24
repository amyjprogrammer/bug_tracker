from django.urls import path

from . import views

app_name = 'issue_tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:ticket_id>/', views.ticket_comment, name="ticket_comment"),
    path('comments/<int:ticket_id>/', views.add_ticket_comment, name="add_ticket_comment"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('add_admin_ticket/<int:ticket_id>/', views.add_admin_ticket, name="add_admin_ticket"),
    path('edit_admin_ticket/<int:ticket_id>/<int:admin_id>/', views.edit_admin_ticket, name="edit_admin_ticket"),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name="delete_ticket"),
]
