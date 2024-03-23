from django.urls import path
from .views import login_view, user_signup, user_logout, change_password

urlpatterns = [
    path("login/", login_view, name="login_url"),
    path("signup/", user_signup, name="signup_url"),
    path("logout/", user_logout, name="logout_url"),
    path("cpass/", change_password, name="cpass_url")
    ]
