# Generated by Django 3.2 on 2021-05-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_alter_message_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]