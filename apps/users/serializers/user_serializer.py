from rest_framework import serializers
from apps.users.models import Users
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'phone')