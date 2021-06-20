from rest_framework import serializers
from .models import *

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields='__all__'

class SubtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields='__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields='__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'