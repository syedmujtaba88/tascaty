"""django imports."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import Activity, ActivityState, ActivityTracker, System, Client
from core.serializers import (ActivitySerializer, ActivityStateSerializer,
                              ActivityTrackerSerializer, SystemSerializer, ClientSerializer)


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

    queryset = ActivityTracker.objects.all()
    serializer_class = ActivityTrackerSerializer
    permission_classes = [
        IsAuthenticated
    ]
