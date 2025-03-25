from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task
from datetime import datetime

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        """Auto-update completed_at if task is marked as completed"""
        if "status" in validated_data and validated_data["status"] == "completed":
            validated_data["completed_at"] = datetime.now()
        return super().update(instance, validated_data)


class TaskAssignSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ['assigned_users']
