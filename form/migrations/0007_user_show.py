# Generated by Django 3.2.4 on 2021-06-20 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_skill_contributed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
