# Generated by Django 3.1.4 on 2021-08-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanbanManager', '0004_auto_20210820_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanbancard',
            name='estimated',
            field=models.IntegerField(default=0),
        ),
    ]
