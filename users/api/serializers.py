from rest_framework import serializers
from users.models import *
from rest_framework import serializers, generics
from users.models import Snippet
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
owner = serializers.ReadOnlyField(source='owner.username')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'owner']
""""
class ourSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'address']#'__all__'
class updateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'address']

"""      
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
