from django.urls import path
from .views import index, contact, search, create, update,\
delete, register, login_view, logout_view, user_update

app_name = "contact"

urlpatterns = [
    path("", index, name="index"),
    path("contact/<int:contact_id>/", contact, name="contact"),
    path("search/", search, name="search"),
    path("contact/create/", create, name="create"),
    path("contact/update<int:contact_id>/", update, name="update"),
    path("contact/delete<int:contact_id>/", delete, name="delete"),
    path("user/create/", register, name="register"),
    path("user/login/", login_view, name="login"),
    path("user/logout/", logout_view, name="logout"),
    path("user/update/", user_update, name="user_update"),
]
