# Generated by Django 4.2.3 on 2023-08-03 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_twitter',
            new_name='social_stackoverflow',
        ),
    ]
