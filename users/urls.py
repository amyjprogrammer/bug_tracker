from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),

    path('logged_out/', auth_views.LogoutView.as_view(template_name="users/logged_out.html"), name="logout"),

    path('register/', user_views.register, name="register"),
]
