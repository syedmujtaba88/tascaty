"""Django Imports."""
from rest_framework import permissions


class ActivityTrackerPermission(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        # add try and except here
        if request.user == obj.username or (request.user.approver == obj.approver
                                            and request.data['status'] in (2, 3)):
            return True
        return False
