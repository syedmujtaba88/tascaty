"""django imports."""
from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserListApi(viewsets.ModelViewSet):
    """Use this class to interact with default UserModel."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPI(ObtainAuthToken):
    """authenticate user request and return a token."""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
