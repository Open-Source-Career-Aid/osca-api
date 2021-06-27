from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(
    [User, Skill, Topic, Subtopic, Resource, Tag, Prerequisite, Super_skill])
