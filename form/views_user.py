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
def post_user_message(request):
    data = request.data
    user_name = data['name']
    user_email = data['email']
    user_message =  data['message']
    message = User_messages(name=user_name, email=user_email, message=user_email)

    message.save("user")
    return Response(status=status.HTTP_201_CREATED)


