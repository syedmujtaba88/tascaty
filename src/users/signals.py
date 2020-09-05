"""django imports."""
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import TeamLead


User = get_user_model()


@receiver(signals.post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    """Update team lead when user's TL is upadated."""
    if not created:
        print(instance)


@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Add a team lead when user is created as TL."""
    qo = User.objects.filter(username=instance, is_team_lead=1).values(
        'first_name', 'last_name')
    if created and qo:
        full_name = qo[0]['first_name'] + ' ' + qo[0]['last_name']
        TeamLead.objects.get_or_create(user_name=instance, fullname=full_name)
    return None
