from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# for the authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# for the api
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *

from .serializers import *


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


# @api_view(['GET', 'POST', 'DELETE',  'PATCH'])
# def job(request):
#     if request.method == 'GET':
#         objects = Job_Model.objects.all()
#         serializer = Job_Serializer(objects, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = request.data
#         serializer = Job_Serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == 'PATCH':
#         data = request.data
#         obj = Job_Model.objects.get(id=data['id'])
#         serializer = Job_Serializer(obj, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == 'DELETE':
#         data = request.data
#         obj = Job_Model.objects.get(id=data['id'])
#         obj.delete()
#         return Response({'message': 'Person is deleted'})
# class Jobviewsets(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = Job_Serializer
#     queryset = Job_Model.objects.all()
class Jobviewsets(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Job_Serializer
    queryset = Job_Model.objects.all()


class Company_viewsets(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Company_Serializer
    queryset = Company_Model.objects.all()


def index(request):
    if request.method == 'POST':
        form = Jobform()(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = Jobform()
    return render(request, 'index.html', {'form': form})
