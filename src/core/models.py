"""django imports."""
from django.db import models
from django.conf import settings
from users.models import TeamLead


class Activity(models.Model):
    """Master Table for Activity types."""

    activity_name = models.CharField(max_length=100, unique=True)


class ActivityState(models.Model):
    """Activity Status Description."""

    state_name = models.CharField(max_length=100, unique=True)


class System(models.Model):
    """Master Table for Systems."""

    system_name = models.CharField(max_length=100, unique=True)


class Client(models.Model):
    """Master Table for clients."""

    client_name = models.CharField(max_length=100, unique=True)


class ActivityTracker(models.Model):
    """Transaction Table to store activites."""

    username = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    approver = models.ForeignKey(
        TeamLead, on_delete=models.DO_NOTHING)
    activity_name = models.ForeignKey(
        Activity, on_delete=models.DO_NOTHING)
    system_name = models.ForeignKey(
        System, on_delete=models.DO_NOTHING)
    client_name = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(
        ActivityState, on_delete=models.DO_NOTHING, default=1)
    date = models.DateField()
    hours = models.IntegerField(null=True)
    minutes = models.IntegerField(null=True)
    no_of_records = models.IntegerField(null=True)
    project = models.CharField(max_length=255, null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        """Human readable return string."""
        return self.activity_name.activity_name
