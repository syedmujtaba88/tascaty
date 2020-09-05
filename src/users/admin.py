"""django imports."""
from django.contrib import admin
from users.models import User, TeamLead

# Register your models here.
admin.site.register(User)
admin.site.register(TeamLead)
