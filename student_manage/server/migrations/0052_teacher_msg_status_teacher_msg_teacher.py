# Generated by Django 4.0.5 on 2022-10-30 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0051_student_msg_teacher_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_msg',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher_msg',
            name='teacher',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='server.teacher'),
        ),
    ]
