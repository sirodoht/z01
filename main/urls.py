from django.urls import path

from main import views

urlpatterns = [
    path("", views.CreateEntry.as_view(), name="index"),
    path("submit-success/", views.submit_success, name="submit_success"),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
]
