# Generated by Django 3.2 on 2021-05-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0004_auto_20210521_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]