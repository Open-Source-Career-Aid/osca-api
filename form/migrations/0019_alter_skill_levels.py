# Generated by Django 3.2.4 on 2021-11-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0018_auto_20211126_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='levels',
            field=models.ManyToManyField(blank=True, related_name='all_levels_with_this_skill', to='form.Level'),
        ),
    ]
