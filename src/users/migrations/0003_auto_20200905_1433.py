# Generated by Django 3.1.1 on 2020-09-05 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_teamleads'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeamLeads',
            new_name='TeamLead',
        ),
    ]
