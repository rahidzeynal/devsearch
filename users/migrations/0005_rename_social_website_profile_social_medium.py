# Generated by Django 4.2.3 on 2023-08-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_social_twitter_profile_social_stackoverflow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_website',
            new_name='social_medium',
        ),
    ]