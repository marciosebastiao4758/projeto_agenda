from django.urls import path
from .views import index, contact, search

app_name = "contact"

urlpatterns = [
    path("", index, name="index"),
    path("contact/<int:contact_id>/", contact, name="contact"),
    path("search/", search, name="search"),
]
