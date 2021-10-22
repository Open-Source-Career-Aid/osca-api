from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from json import loads


@api_view(['POST'])
def post_skill_edits(request):
    data = request.data
    name = data['userName']
    organization_name = data['organization_name']
    branch_name = data['branch_name']
    program_duration = data['program_duration']
    show = data['show']
    user = User(userName=name, branch_name=branch_name,
                organization_name=organization_name, program_duration=program_duration, show=show)
    user.save(using='edits')

    skill_name = data['skill']
    skill = Skill(contributed_by=user, skill=skill_name)
    skill.save(using='edits')

    for tag in data['tags']:
        tagObj = Tag.objects.using('edits').filter(tagName=tag['tagName'])
        if not tagObj:
            tagObj = Tag.objects.using('edits').create(tagName=tag['tagName'].lower())
            skill.tags.add(tagObj)
        else:
            skill.tags.add(tagObj[0])
        skill.save(using='edits')

    for prereq in data['prerequisites']:
        pre = Prerequisite.objects.using('edits').filter(prereqName=prereq['prereqName'])
        if not pre:
            pre = Prerequisite.objects.using('edits').create(
                prereqName=prereq['prereqName'].lower())
            skill.prerequisites.add(pre)
        else:
            skill.prerequisites.add(pre[0])
        skill.save(using='edits')

    for topic in data['topics']:
        val = topic['topicName']
        top = Topic(topicName=val)
        top.save(using='edits')
        for resource in topic['resources']:
            res = Resource(link=resource['link'])
            res.save(using='edits')
            top.resources.add(res)
            top.save(using='edits')

        skill.topics.add(top)
        try:
            for y in topic['subtopics']:
                val = y['value']
                sub = Subtopic(value=val)
                sub.save(using='edits')
                for yres in y['resources']:
                    res = Resource(link=yres['value'])
                    res.save(using='edits')
                    sub.resources.add(res)
                    sub.save(using='edits')
                top.subtopics.add(sub)
                top.save(using='edits')
        except KeyError:
            pass

        skill.topics.add(top)
        skill.save(using='edits')
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def post_super_skill_edits(request):
    data = request.data
    name = data['userName']
    onSuperskill=data['OnSuperskill']
    organization_name = data['organization_name']
    branch_name = data['branch_name']
    program_duration = data['program_duration']
    show = data['show']

    user = User(userName=name, branch_name=branch_name,
                organization_name=organization_name, program_duration=program_duration, show=show)
    user.save(using='edits')

    super_skill_name = data['super_skill']
    super_skill = Super_skill_edit(name=super_skill_name, contributed_by=user,on_id=int(onSuperskill))
    super_skill.save(using='edits')

    for tag in data['tags']:
        tagObj = Tag.objects.using('edits').filter(tagName=tag['tagName'])
        if not tagObj:
            tagObj = Tag.objects.using('edits').create(tagName=tag['tagName'].lower())
            super_skill.tags.add(tagObj)
        else:
            super_skill.tags.add(tagObj[0])
        super_skill.save(using='edits')

    for sub_skill in data['roadmap']:
        skill = Skill.objects.using('edits').filter(skill=sub_skill['skillName'])
        if not skill:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            super_skill.sub_skills.add(skill[0])
        super_skill.save(using='edits')

    if "prerequisites" in data:
        for prereq in data['prerequisites']:
            pre = Prerequisite.objects.using('edits').filter(prereqName=prereq['prereqName'])
            if not pre:
                pre = Prerequisite.objects.using('edits').create(
                    prereqName=prereq['prereqName'].lower())
                super_skill.prerequisites.add(pre)
            else:
                super_skill.prerequisites.add(pre[0])
            super_skill.save(using='edits')
    return Response(status=status.HTTP_201_CREATED)