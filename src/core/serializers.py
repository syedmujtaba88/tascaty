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
        fields = ('id', 'username', 'approver', 'activity_name', 'system_name',
                  'client_name', 'status', 'date', 'hours', 'minutes', 'no_of_records', 'project', 'comments')
        extra_kwargs = {
            'id': {'read_only': True},
        }


'''
    def create(self, validated_data):
        """Add a new user and return auth token."""
        """username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            username, email, password, **validated_data)
        return user"""
        pass

    def update(self, instance, validated_data):
        """Handle updating user account."""
        """if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)"""
        pass
'''
