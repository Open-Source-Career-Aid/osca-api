from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_user_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super_skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('sub_skills', models.ManyToManyField(related_name='super_skill', to='form.Skill')),
            ],
        ),
    ]
