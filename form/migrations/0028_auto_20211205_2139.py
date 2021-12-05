# Generated by Django 3.2.5 on 2021-12-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0027_auto_20211205_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
