# Generated by Django 3.2 on 2021-05-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_auto_20210512_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]