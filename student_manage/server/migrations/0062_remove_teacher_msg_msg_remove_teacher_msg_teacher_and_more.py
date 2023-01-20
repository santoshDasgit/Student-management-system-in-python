# Generated by Django 4.1.2 on 2022-11-04 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0061_teacher_msg_msg_teacher_msg_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_msg',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='teacher_msg',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='teacher_msg',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Teacher_see_msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('msg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.teacher_msg')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.teacher')),
            ],
        ),
    ]
