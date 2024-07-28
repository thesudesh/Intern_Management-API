from rest_framework.permissions import BasePermission

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'supervisor'

class IsIntern(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'intern'
