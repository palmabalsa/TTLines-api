# Generated by Django 4.0.3 on 2022-09-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trout', '0005_alter_fishinglogentry_any_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishinglogentry',
            name='fish_condition',
            field=models.CharField(blank=True, choices=[('Spent', 'Spent'), ('Average', 'Average'), ('Good', 'Good'), ('Sashimi(Excellent)', 'Sashimi(Excellent)')], default=None, max_length=18, null=True),
        ),
    ]