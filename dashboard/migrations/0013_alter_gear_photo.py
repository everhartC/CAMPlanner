# Generated by Django 3.2 on 2021-05-23 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_gear_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
