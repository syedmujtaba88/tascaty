"""django imports."""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class TeamLead(models.Model):
    """Team Leads model."""

    # user_name = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, unique=True)
    user_name = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(null=False, max_length=100)

    def __str__(self):
        """Human readable return string."""
        return self.fullname


class User(AbstractUser):
    """User model abstracted from django aut user."""

    is_team_lead = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    approver = models.ForeignKey(
        TeamLead, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        """Human readable return string."""
        return self.username
