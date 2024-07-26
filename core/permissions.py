from rest_framework.permissions import BasePermission

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Supervisor'

class IsIntern(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Intern'
