from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from apps.users.serializers.user_serializer import UserSerializer
from apps.users.services.create import CreateUser
from apps.users.services.update import UpdateUser
from rest_framework.utils import json

from .exceptions import RecordSaveError
from .models import Users

# Create your views here.
@api_view(['GET'])
def index(request):
    users = Users.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def create(request):
    try:
        user = CreateUser(request.data).execute()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except RecordSaveError as error:
        res = {'code':422, 'message': error.message}
        return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        res = {'code': 500, 'message': 'Unexpected error'}
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def detail(request, id):
    try:
        user = Users.objects.get(id=id)
    except ObjectDoesNotExist:
        res = {'code': 404, 'message': 'not found'}
        return Response(res, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update(request, id):
    try:
        user = UpdateUser(id, request.data).execute()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except RecordSaveError as error:
        res = {'code': 422, 'message': error.message}
        return Response(json.dumps(res), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        res = {'code': 500, 'message': 'Unexpected error'}
        return Response(json.dumps(res), status=status.HTTP_500_INTERNAL_SERVER_ERROR)