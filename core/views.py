# core/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import UserProfile, Task, Attendance
from .serializers import UserProfileSerializer, TaskSerializer, AttendanceSerializer
from .permissions import IsSupervisor, IsIntern

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsIntern])
    def mark_as_complete(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        return Response({'status': 'Task marked as complete'})

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsIntern])
    def check_in(self, request):
        user = request.user
        attendance = Attendance.objects.create(user=user)
        return Response({'status': 'Checked in', 'attendance_id': attendance.id})

    @action(detail=True, methods=['post'], permission_classes=[IsIntern])
    def check_out(self, request, pk=None):
        attendance = self.get_object()
        attendance.check_out_time = timezone.now()
        attendance.save()
        return Response({'status': 'Checked out'})
