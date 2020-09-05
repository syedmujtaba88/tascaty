# Generated by Django 3.1.1 on 2020-09-05 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamlead',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]