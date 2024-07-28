from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, TaskViewSet, AttendanceViewSet, LoginView, LogoutView

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'attendances', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
