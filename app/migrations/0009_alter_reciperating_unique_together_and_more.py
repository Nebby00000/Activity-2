# Generated by Django 5.1.1 on 2024-11-27 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_reciperating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reciperating',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='visibility',
        ),
    ]
