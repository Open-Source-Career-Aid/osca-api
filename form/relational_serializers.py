from rest_framework import serializers
from .models import *

class TagSerializer(serializers.RelatedField):

     def to_representation(self, value):
         return value.value

     class Meta:
        model = Tag

class RelationalSubSkillSerializer(serializers.RelatedField):
     def to_representation(self, value):
         return value.skill

     class Meta:
        model = Skill

class RelationalPrerequisiteSerializer(serializers.RelatedField):
     def to_representation(self, value):
         return value.value

     class Meta:
        model = Prerequisite