from django.urls import path

from . import views,models

urlpatterns = [
    path("coll", models.coll,name="collect")
]