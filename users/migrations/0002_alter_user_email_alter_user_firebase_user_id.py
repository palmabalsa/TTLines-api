# Generated by Django 4.0.3 on 2022-08-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='firebase_user_id',
            field=models.CharField(max_length=300, primary_key=True, serialize=False, unique=True),
        ),
    ]