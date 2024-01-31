# authorized
from django.contrib.auth.models import Group, User
# not authorized
from my_rest_app.models import TestExample
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TestExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestExample
        fields = ['nickname', 'country']
