from django.urls import path, include
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("", views.index, name="index"),
    path("", include("django.contrib.auth.urls"))
]
