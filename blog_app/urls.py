from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="board"),
    path("post/", views.post_page, name="post"),
]
