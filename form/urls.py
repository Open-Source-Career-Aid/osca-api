from django.urls import path

from . import views,models

urlpatterns = [
    path("add-new-skill/", views.post_skill,name="add new skill"),
]