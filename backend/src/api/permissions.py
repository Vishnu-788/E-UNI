from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }



class IsVerifiedShop(permissions.BasePermission):
    message = "You must be a verified shop to perform this action."
    def has_permission(self, request, view):
        user = request.user
        return hasattr(user, 'shop') and user.shop.is_verified


# class IsNormalUserPermission(permissions.DjangoModelPermissions):
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': [],
#         'HEAD': [],
#         'POST': [],
#         'PUT': [],
#         'PATCH': [],
#         'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }

