"""django imports."""
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token as auth_token
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import TeamLead
from users.serializers import UserSerializer, TeamLeadSerializer


User = get_user_model()


class UserListApi(viewsets.ModelViewSet):
    """Use this class to interact with default UserModel."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        """Filter objects of current authenticated user only."""
        return self.queryset  # .filter(username=self.request.user)


class UserLoginAPI(ObtainAuthToken):
    """authenticate user request and return a token."""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LogoutView(APIView):
    """Logout the authenticated user."""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """Logout method - delete operation for generated token."""
        token_key = request.headers['Authorization'].split()[1]
        auth_token.objects.get(key=token_key).delete()
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data)


class TeamLeadsApi(viewsets.ModelViewSet):
    """Use this class to interact with TeamLeads Model."""

    queryset = TeamLead.objects.all()
    serializer_class = TeamLeadSerializer
    permission_classes = [
        IsAuthenticated
    ]
