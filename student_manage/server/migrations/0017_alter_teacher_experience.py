# Generated by Django 4.1.2 on 2022-10-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_teacher_experience_teacher_id_teacher_join_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.IntegerField(default=None),
        ),
    ]
