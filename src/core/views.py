"""django imports."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import Activity, ActivityState, ActivityTracker, System, Client
from core.serializers import (ActivitySerializer, ActivityStateSerializer,
                              ActivityTrackerSerializer, SystemSerializer, ClientSerializer)
from core.permissions import ActivityTrackerPermission


class ActivityApi(viewsets.ModelViewSet):
    """Use this class to register activities master data."""

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [
        IsAuthenticated
    ]


class ActivityStateApi(viewsets.ModelViewSet):
    """Use this class to register Activity status description."""

    queryset = ActivityState.objects.all()
    serializer_class = ActivityStateSerializer
    permission_classes = [
        IsAuthenticated
    ]


class SystemApi(viewsets.ModelViewSet):
    """Use this class to register System master data."""

    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = [
        IsAuthenticated
    ]


class ClientApi(viewsets.ModelViewSet):
    """Use this class to register Client master data."""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated
    ]


class ActivityTrackerApi(viewsets.ModelViewSet):
    """Use this class to register daily activities of users."""

    permission_classes = [
        ActivityTrackerPermission, IsAuthenticated
    ]
    queryset = ActivityTracker.objects.all()
    serializer_class = ActivityTrackerSerializer

    def perform_create(self, serializer):
        """Set the user,status,approver to the logged in user."""
        if self.request.user.is_team_lead:
            serializer.save(username=self.request.user,
                            approver=self.request.user.approver,
                            status=ActivityState.objects.get(pk=3))
        serializer.save(username=self.request.user,
                        approver=self.request.user.approver)
