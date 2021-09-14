from django.urls import path

from . import views


urlpatterns = [
    path("", views.CreateProView.as_view(),),
    path("list", views.ProfileView.as_view(),)
] 
