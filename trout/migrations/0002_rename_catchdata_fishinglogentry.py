# Generated by Django 4.0.3 on 2022-08-02 04:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CatchData',
            new_name='FishingLogEntry',
        ),
    ]
