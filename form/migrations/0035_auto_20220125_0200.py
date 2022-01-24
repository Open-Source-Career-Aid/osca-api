# Generated by Django 3.2.4 on 2022-01-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0034_auto_20211207_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagName',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
