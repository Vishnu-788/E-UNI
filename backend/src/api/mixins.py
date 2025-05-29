from .permissions import IsStaffEditorPermission
from rest_framework import permissions

class IsStaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

class IsNormalUserPermissionMixin:
    permissions_classes = []