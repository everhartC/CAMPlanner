# Generated by Django 3.2 on 2021-05-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210522_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
    ]