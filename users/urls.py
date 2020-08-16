from django.urls import path
from .api.viewsets import LoginView, RegisterView

urlpatterns = [
    path('signup', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]