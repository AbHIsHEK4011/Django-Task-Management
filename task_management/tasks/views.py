from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, User
from .serializers import TaskSerializer, TaskAssignSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """Override this method if you want to add custom logic on update"""
        serializer.save()


class TaskAssignViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserTasksViewSet(viewsets.ViewSet):
    def list(self, request, user_id=None):
        user = get_object_or_404(User, pk=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)



User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to register
