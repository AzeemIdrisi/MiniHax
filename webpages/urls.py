from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("details/<int:id>/", views.details, name="details"),
    path("schedule/<int:id>/", views.schedule, name="schedule"),
]
