"""django imports."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import TeamLead

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for users api."""

    class Meta:
        """defines meta details for parent class object."""

        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name',
                  'last_name', 'password', 'approver', 'is_team_lead')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True,
                         'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        """Add a new user and return auth token."""
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            username, email, password, **validated_data)
        return user

    def update(self, instance, validated_data):
        """Handle updating user account."""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class TeamLeadSerializer(serializers.ModelSerializer):
    """Serializer for TeamLead api."""

    class Meta:
        """defines meta details for parent class object."""

        model = TeamLead
        fields = ('id', 'user_name', 'fullname')
        extra_kwargs = {
            'id': {'read_only': True},
        }
