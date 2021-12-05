# Generated by Django 3.2.5 on 2021-12-05 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('form', '0024_auto_20211204_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopic',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='vote_score',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='vote_score',
        ),
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, 'Dislike'), (1, 'Like')], verbose_name='vote')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.user', verbose_name='user')),
            ],
        ),
    ]
