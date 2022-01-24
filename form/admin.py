from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import *

class SkillAdmin(OrderedModelAdmin):
    list_display = ('skill', 'move_up_down_links')
class Super_skillAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')
class TagAdmin(OrderedModelAdmin):
    list_display = ('tagName', 'move_up_down_links')
class PrerequisiteAdmin(OrderedModelAdmin):
    list_display = ('prereqName', 'move_up_down_links')
class TopicAdmin(OrderedModelAdmin):
    list_display = ('topicName', 'move_up_down_links')
class SubtopicAdmin(OrderedModelAdmin):
    list_display = ('value', 'move_up_down_links')
class User_messagesAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')


# Register your models here.
admin.site.register(User)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Subtopic, SubtopicAdmin)
admin.site.register(Resource)
admin.site.register(Tag, TagAdmin)
admin.site.register(Prerequisite, PrerequisiteAdmin)
admin.site.register(Super_skill, Super_skillAdmin)
admin.site.register(Level)
admin.site.register(User_messages, User_messagesAdmin)
admin.site.register(Vote)
##admin.site.register(Super_skill_edit)
