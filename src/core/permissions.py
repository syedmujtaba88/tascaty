"""Django Imports."""
from rest_framework import permissions


class ActivityTrackerPermission(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        if request.user == obj.username or (request.user.approver == obj.approver
                                            and request.data['status'] == 3):  # add try and catch here
            return True
        return False
