# Generated by Django 3.1.1 on 2020-09-05 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200905_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='approver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teamlead'),
        ),
    ]
