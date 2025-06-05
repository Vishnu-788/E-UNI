from .permissions import IsStaffEditorPermission, IsVerifiedShop
from rest_framework import permissions

class IsStaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

class IsVerifiedShopMixin:
    permission_classes = [IsVerifiedShop]