from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# import json

# Create your views here.
@api_view(['GET', 'POST'])
def post_skill(request):
    if request.method == 'GET':
        skills = Skill.objects.all()
        serialized_data = SkillSerializer(skills, many=True)
        return Response(serialized_data.data)
    elif request.method == 'POST':
        data = request.data

        name= data['name']
        organization_name=data['organization_name']
        branch_name=data['branch_name']
        program_duration=data['program_duration']
        show=data['show']
        user = User(name=name, branch_name=branch_name, organization_name=organization_name,program_duration=program_duration, show=show)
        user.save()

        skill_name=data['skill']
        skill = Skill(contributed_by=user, skill=skill_name)
        skill.save()

        for tag in data['tags']:
            tagObj = Tag(value=tag)
            tagObj.save()
            skill.tags.add(tagObj)
            skill.save()

        for prereq in data['prerequisites']:
            preObj = Prerequisite(value=prereq)
            preObj.save()
            skill.prerequisites.add(preObj)
            skill.save()
            
        for x in data['detail']:
            val = x['value']
            top = Topic(value = val)
            top.save()
            for y in x['resources']:
                res = Resource(value=y['value'])
                res.save()
                top.resources.add(res)
                top.save()

            for y in x['subtopics']:
                val = y['value']
                sub = Subtopic(value=val)
                sub.save()
                for yres in y['resources']:
                    res = Resource(value=yres['value'])
                    res.save()
                    sub.resources.add(res)
                    sub.save()
                top.subtopics.add(sub)
                top.save()

            skill.detail.add(top)
            skill.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_suggestions(request):
    query=request.GET.get('query')
    