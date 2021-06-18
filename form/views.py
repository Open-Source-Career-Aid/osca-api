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
        users = User.objects.all()
        serialized_data = UserSerializer(users, many=True)
        return Response(serialized_data.data)
    elif request.method == 'POST':
        data = request.data

        name= data['name']
        organizationName=data['organizationName']
        branchName=data['branchName']
        skill=data['skill']


        user = User(name=name, branchName=branchName, organizationName=organizationName, skill=skill)
        user.save()
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

            user.detail.add(top)
            user.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)
