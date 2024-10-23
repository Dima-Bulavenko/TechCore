from django.urls import path

from users import views

urlpatterns = [
    path("", views.UserProfile.as_view(), name="user_profile"),
    path("delete/", views.DeleteAccount.as_view(), name="delete_account"),
]
