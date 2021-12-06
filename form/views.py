from django.db.models.fields import EmailField
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from json import loads
from django.db.models import F


# import json

# Create your views here.


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_skill(request):
    data = request.data
    name = data['userName']
    organization_name = data['organization_name']
    branch_name = data['branch_name']
    program_duration = data['program_duration']
    show = data['show']
    user = User(userName=name, branch_name=branch_name,
                organization_name=organization_name, program_duration=program_duration, show=show)
    user.save()

    skill_name = data['skill']
    skill_language = data['language']
    skill = Skill(contributed_by=user, skill=skill_name, language=skill_language)
    skill.save()

    for tag in data['tags']:
        tagObj = Tag.objects.filter(tagName=tag['tagName'])
        if not tagObj:
            tagObj = Tag.objects.create(tagName=tag['tagName'].lower())
            skill.tags.add(tagObj)
        else:
            skill.tags.add(tagObj[0])
        skill.save()

    for prereq in data['prerequisites']:
        pre = Prerequisite.objects.filter(prereqName=prereq['prereqName'])
        if not pre:
            pre = Prerequisite.objects.create(
                prereqName=prereq['prereqName'].lower())
            skill.prerequisites.add(pre)
        else:
            skill.prerequisites.add(pre[0])
        skill.save()

    for level in data['levels']:
        val = level['levelName']
        # temp1_vote = Vote()
        lev = Level(levelName=val)
        lev.save()
        
        for topic in level['topics']:
            val = topic['topicName']
            temp2_vote = Vote()
            top = Topic(topicName=val, topic_vote= temp2_vote)
            temp2_vote.save()
            top.save()
            try:
                for resource in topic['resources']:
                    temp3_vote = Vote()
                    res = Resource(link=resource['link'], resource_vote = temp3_vote)
                    temp3_vote.save()
                    res.save()
                    top.resources.add(res)
                    top.save()
            except KeyError:
                pass
            lev.topics.add(top)
            try:
                for y in topic['subtopics']:
                    temp4_vote = Vote()
                    val = y['value']
                    sub = Subtopic(value=val, subtopic_vote=temp4_vote)
                    temp4_vote.save()
                    sub.save()
                    for yres in y['resources']:
                        temp5_vote = Vote()
                        res = Resource(link=yres['link'], resource_vote = temp5_vote)
                        temp5_vote.save()
                        res.save()
                        sub.resources.add(res)
                        sub.save()
                    top.subtopics.add(sub)
                    top.save()
            except KeyError:
                pass

            lev.topics.add(top)
            lev.save()
        skill.levels.add(lev)
        skill.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_all_skills(request):
    skills = Skill.objects.all()
    serialized_data = SkillSerializer(skills, many=True)
    return Response(serialized_data.data)


@api_view(['GET'])
def get_all_super_skills(request):
    skills = Super_skill.objects.all()
    serialized_data = SuperSkillSerializer(skills, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_super_skill(request):
    data = request.data
    name = data['userName']
    organization_name = data['organization_name']
    branch_name = data['branch_name']
    program_duration = data['program_duration']
    show = data['show']

    user = User(userName=name, branch_name=branch_name,
                organization_name=organization_name, program_duration=program_duration, show=show)
    user.save()

    super_skill_name = data['super_skill']
    super_skill = Super_skill(name=super_skill_name, contributed_by=user)
    super_skill.save()

    for tag in data['tags']:
        tagObj = Tag.objects.filter(tagName=tag['tagName'])
        if not tagObj:
            tagObj = Tag.objects.create(tagName=tag['tagName'].lower())
            super_skill.tags.add(tagObj)
        else:
            super_skill.tags.add(tagObj[0])
        super_skill.save()

    for sub_skill in data['roadmap']:
        skill = Skill.objects.filter(skill=sub_skill['skillName'])
        if not skill:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            super_skill.sub_skills.add(skill[0])
        super_skill.save()

    if "prerequisites" in data:
        for prereq in data['prerequisites']:
            pre = Prerequisite.objects.filter(prereqName=prereq['prereqName'])
            if not pre:
                pre = Prerequisite.objects.create(
                    prereqName=prereq['prereqName'].lower())
                super_skill.prerequisites.add(pre)
            else:
                super_skill.prerequisites.add(pre[0])
            super_skill.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_suggestions(request):
    query = request.GET.get('query')
    skills = Skill.objects.filter(skill__icontains=query)
    serialized_skill_data = SkillSerializer(skills, many=True)
    super_skills = Super_skill.objects.filter(name__icontains=query)
    serialized_superskill_data = SuperSkillSerializer(super_skills, many=True)
    return Response({"skills": serialized_skill_data.data, "super_skills": serialized_superskill_data.data})


@api_view(['GET'])
def get_super_skill(request):
    id = request.GET.get('id')
    super_skills = Super_skill.objects.filter(id=id)
    serialized_superskill_data = SuperSkillSerializer(super_skills, many=True)
    if(serialized_superskill_data.data):
        return Response(serialized_superskill_data.data[0])
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_skill(request):
    id = request.GET.get('id')
    skills = Skill.objects.filter(id=id)
    serialized_skill_data = SkillSerializer(skills, many=True)
    if(serialized_skill_data.data):
        return Response(serialized_skill_data.data[0])
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def learn_skill(request):
    search_data = request.GET.get('searchData')
    skills = Skill.objects.filter(skill__startswith=search_data)
    serialized_skill_data = SkillNameSerializer(skills, many=True)
    for i in range(len(serialized_skill_data.data)):
        serialized_skill_data.data[i].update({"is_superskill": False})
    super_skills = Super_skill.objects.filter(name__startswith=search_data)
    serialized_superskill_data = SuperSkillNameSerializer2(
        super_skills, many=True)
    for i in range(len(serialized_superskill_data.data)):
        serialized_superskill_data.data[i].update({"is_superskill": True})
    serialized_data = serialized_skill_data.data + serialized_superskill_data.data
    if(serialized_data):
        return Response(serialized_data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_vote_resource(request):
    data = request.data
    upvote_or_downvote = data['type']
    id_obj = data['id']
    vote_obj = Resource.objects.get(id=id_obj)
    
    # print(vote_obj)
    if(upvote_or_downvote == 1):
        vote_obj.like = vote_obj.like + 1
    else:
        vote_obj.dislike = vote_obj.dislike + 1
    vote_obj.save()

    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def post_vote_subtopic(request):
    data = request.data
    upvote_or_downvote = data['type']
    id_obj = data['id']
    vote_obj = Subtopic.objects.get(id=id_obj)
    
    # print(vote_obj)
    if(upvote_or_downvote == 1):
        vote_obj.like = vote_obj.like + 1
    else:
        vote_obj.dislike = vote_obj.dislike + 1
    vote_obj.save()

    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def post_vote_topic(request):
    data = request.data
    upvote_or_downvote = data['type']
    id_obj = data['id']
    vote_obj = Topic.objects.get(id=id_obj)
    
    # print(vote_obj)
    if(upvote_or_downvote == 1):
        vote_obj.like = vote_obj.like + 1
    else:
        vote_obj.dislike = vote_obj.dislike + 1
    vote_obj.save()

    return Response(status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_votes(request):
    votes = Vote.objects.all()
    serialized_data = VoteSerializer(votes, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_resources(request):
    votes = Resource.objects.all()
    serialized_data = ResourceSerializer(votes, many=True)
    return Response(serialized_data.data)
