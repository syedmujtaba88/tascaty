"""django imports."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Activity, ActivityState, ActivityTracker, System, Client

User = get_user_model()


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity Master."""

    class Meta:
        """defines meta details for parent class object."""

        model = Activity
        fields = ('id', 'activity_name')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client Master."""

    class Meta:
        """defines meta details for parent class object."""

        model = Client
        fields = ('id', 'client_name')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class SystemSerializer(serializers.ModelSerializer):
    """Serializer for System Master."""

    class Meta:
        """defines meta details for parent class object."""

        model = System
        fields = ('id', 'system_name')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ActivityStateSerializer(serializers.ModelSerializer):
    """Serializer for ActivityState Master."""

    class Meta:
        """defines meta details for parent class object."""

        model = ActivityState
        fields = ('id', 'state_name')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ActivityTrackerSerializer(serializers.ModelSerializer):
    """Serializer for Activity Tracker."""

    class Meta:
        """defines meta details for parent class object."""

        model = ActivityTracker
        fields = ('id', 'username', 'approver', 'status', 'activity_name', 'system_name',
                  'client_name', 'date', 'hours', 'minutes', 'no_of_records', 'project', 'comments')
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'approver': {'read_only': True},
            'status': {'required': False}
        }
