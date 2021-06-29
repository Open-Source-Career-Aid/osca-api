from django.urls import path

from . import views,models

urlpatterns = [
    path("add-new-skill/", views.post_skill,name="add new skill"),
    path("get-suggestions/", views.get_suggestions,name="get suggestions"),
    path("get-super-skill/", views.get_super_skill,name="get super skill"),
    path("get-skill/", views.get_skill,name="get skill"),
]