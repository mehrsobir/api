from django.urls import path
from .views import CustomUserCreate, LoginView, LogoutView
from django.contrib.auth.views import auth_login

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]