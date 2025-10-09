from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write allowed only to the object's author/owner
        return getattr(obj, 'author', None) == request.user
