# Generated by Django 3.1.6 on 2021-05-21 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210521_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='slug',
        ),
    ]