from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Resource
from .serializers import ResourceSerialzer

@api_view(['GET', 'POST'])
def resources(request):
    if request.method == 'GET': # user requesting data 
        snippets = Resource.objects.all()
        serializer = ResourceSerialzer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # user posting data
        serializer = ResourceSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
