from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "dynamic-form/",
        views.dynamic_form,
        name="dynamic_form"
    ),
    path(
        "registration/",
        include("registration.urls")
    ),
]