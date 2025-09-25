from django.urls import path
from .user_views import RegisterView, CurrentUserView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="auth_register"),
    path("auth/me/", CurrentUserView.as_view(), name="auth_me"),
]
