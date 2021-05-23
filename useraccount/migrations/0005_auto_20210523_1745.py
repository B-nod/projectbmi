# Generated by Django 3.2 on 2021-05-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0004_profile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
