# Generated by Django 3.2 on 2021-05-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0005_auto_20210523_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=255, null=True),
        ),
    ]
