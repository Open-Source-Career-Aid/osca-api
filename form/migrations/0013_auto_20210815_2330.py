# Generated by Django 3.2.4 on 2021-08-15 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_auto_20210720_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prerequisite',
            old_name='value',
            new_name='prereqName',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='value',
            new_name='tagName',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='value',
            new_name='topicName',
        ),
    ]