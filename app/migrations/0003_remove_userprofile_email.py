# Generated by Django 5.1.1 on 2024-10-26 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
