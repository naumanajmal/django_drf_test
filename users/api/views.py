from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import serializers, status, generics
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import *
from users.api.serializers import *
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
class SnippetList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SnippetDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """
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

    """
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 