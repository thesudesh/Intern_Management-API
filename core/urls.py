from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, TaskViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'attendances', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
