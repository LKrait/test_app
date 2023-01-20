from django.urls import path, include
from . import views


urlpatterns = [
path('user_login/', views.login_user, name="login")
]
