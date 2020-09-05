
"""django imports."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Config for Users App."""

    name = 'users'

    def ready(self):
        """Call signals from singnal py file."""
        import users.signals  # noqa
