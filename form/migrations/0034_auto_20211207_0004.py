# Generated by Django 3.2.5 on 2021-12-06 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0033_remove_vote_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='id',
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_vote',
            field=models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.PROTECT, parent_link=True, primary_key=True, related_name='vote_topic', serialize=False, to='form.vote'),
        ),
    ]
