from django.urls import path

from . import views,models

urlpatterns = [
    path("add-new-skill/", views.post_skill,name="add new skill"),
    path("add-new-super-skill/", views.post_super_skill,name="add new super skill"),
]