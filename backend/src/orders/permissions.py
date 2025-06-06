from rest_framework import permissions
from users.models import User


class IsShopPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Role.SHOP

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and
            request.user.role == 'shop' and
            obj.shop.user == request.user
        )
    
class IsCustomerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Role.CUSTOMER
    
