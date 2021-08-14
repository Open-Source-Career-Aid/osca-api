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
        name= data['userName']
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
            try:
                tagObj = Tag.objects.get(value=tag)
            except Tag.DoesNotExist:
                tagObj = Tag(value=tag.lower())
                tagObj.save()
            finally:
                skill.tags.add(tagObj)
                skill.save()

        for prereq in data['prerequisites']:
            try:
                pre = Prerequisite.objects.get(value=prereq)
            except Prerequisite.DoesNotExist:
                pre = Prerequisite(value=prereq.lower())
                pre.save()
            finally:
                skill.prerequisites.add(pre)
                skill.save()
            
        for topic in data['topics']:
            val = topic['topicName']
            top = Topic(value = val)
            top.save()
            for resource in topic['resources']:
                res = Resource(value=resource['link'])
                res.save()
                top.resources.add(res)
                top.save()


            skill.topics.add(top)
            try:
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
            except KeyError:
                pass

            skill.detail.add(top)
            skill.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def post_super_skill(request):
    if request.method == 'GET':
        skills = Super_skill.objects.all()
        serialized_data = SuperSkillSerializer(skills, many=True)
        return Response(serialized_data.data)
    if request.method == 'POST':
        data = request.data

        name= data['name']
        organization_name=data['organization_name']
        branch_name=data['branch_name']
        program_duration=data['program_duration']
        show = data['show']

        user = User(name=name, branch_name=branch_name, organization_name=organization_name,program_duration=program_duration,show=show)
        user.save()

        super_skill_name = data['super_skill']
        super_skill = Super_skill(name=super_skill_name)
        super_skill.save()

        
        for tag in data['tags']:
            try:
                tagObj = Tag.objects.get(value=tag['tagName'])
            except Tag.DoesNotExist:
                tagObj = Tag(value=tag.lower())
                tagObj.save()
            finally:
                super_skill.tags.add(tagObj)
                super_skill.save()

        for sub_skill in data['roadmap']:
            try:
                skill = Skill.objects.get(skill=sub_skill['skillName'])
                super_skill.sub_skills.add(skill)
                super_skill.save()
            except Skill.DoesNotExist:
                return Response(status = status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_suggestions(request):
    query=request.GET.get('query')
    skills=Skill.objects.filter(skill__icontains=query)
    serialized_skill_data = SkillNameSerializer(skills, many=True)
    super_skills=Super_skill.objects.filter(name__icontains=query)
    serialized_superskill_data = SuperSkillNameSerializer(super_skills, many=True)
    return Response({"skills":serialized_skill_data.data,"super_skills":serialized_superskill_data.data})


@api_view(['GET'])
def get_super_skill(request):
    id=request.GET.get('id')
    super_skills=Super_skill.objects.filter(id=id)
    serialized_superskill_data = SuperSkillSerializer(super_skills, many=True)
    if(serialized_superskill_data.data):
        return Response(serialized_superskill_data.data[0])
    return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_skill(request):
    id=request.GET.get('id')
    skills=Skill.objects.filter(id=id)
    serialized_skill_data = SkillSerializer(skills, many=True)
    if(serialized_skill_data.data):
        return Response(serialized_skill_data.data[0])
    return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def learn_skill(request):
    search_data = request.GET.get('searchData')
    skills = Skill.objects.filter(skill__startswith=search_data)
    serialized_skill_data = SkillNameSerializer(skills, many=True)
    for i in range(len(serialized_skill_data.data)):
        serialized_skill_data.data[i].update({"is_superskill" : False})
    super_skills = Super_skill.objects.filter(name__startswith=search_data)
    serialized_superskill_data = SuperSkillNameSerializer2(super_skills, many=True)
    for i in range(len(serialized_superskill_data.data)):
        serialized_superskill_data.data[i].update({"is_superskill" : True})
    serialized_data = serialized_skill_data.data + serialized_superskill_data.data
    if(serialized_data):
        return Response(serialized_data)
    return Response(status = status.HTTP_404_NOT_FOUND)