# Generated by Django 3.2.4 on 2021-11-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0019_alter_skill_levels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='topics_level', to='form.Topic'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='levels',
            field=models.ManyToManyField(blank=True, related_name='all_skills_with_this_level', to='form.Level'),
        ),
    ]
