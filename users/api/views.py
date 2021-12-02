from django.http.response import JsonResponse
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import *
from users.api.serializers import *
def myview(request):
    return JsonResponse("api base point", safe =False)
@api_view(['GET'])
def api_details_view(request):
    namelist = User.objects.all()
    serializer = ourSerializer(namelist, many=True)
    return Response(serializer.data)
@api_view(['POST', 'GET'])
def api_update_view(request, pk):
    name = User.objects.get(id=pk)
    serializer = updateSerializer(instance=name, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
