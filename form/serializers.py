from django.db.models import fields
from rest_framework import serializers
from .models import *
from .relational_serializers import *

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
    tag = TagSerializer(source="tags",read_only=True, many=True)
    prerequisite = RelationalPrerequisiteSerializer(source="prerequisites",read_only=True, many=True)
    class Meta:
        model = Skill
        fields=('id','contributed_by','skill','tag','prerequisite','detail')
        depth = 2

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class SuperSkillSerializer(serializers.ModelSerializer):
    tag = TagSerializer(source="tags",read_only=True, many=True)
    sub_skill= RelationalSubSkillSerializer(source="sub_skills",read_only=True, many=True)
    class Meta:
        model = Super_skill
        fields = ('id','contributed_by','name','tag','sub_skill')
        depth=1

class SkillNameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(source="tags",read_only=True, many=True)
    class Meta:
        model = Skill
        fields = ['id','skill','tag']

class SuperSkillNameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(source="tags",read_only=True, many=True)
    sub_skill= RelationalSubSkillSerializer(source="sub_skills",read_only=True, many=True)
    class Meta:
        model = Super_skill
        fields = ['id','name','tag','sub_skill']
