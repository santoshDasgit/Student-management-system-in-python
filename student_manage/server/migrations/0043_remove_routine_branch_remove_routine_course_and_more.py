# Generated by Django 4.0.5 on 2022-10-27 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0042_alter_subject_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='course',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='sem',
        ),
        migrations.CreateModel(
            name='Routine_head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.branch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.course')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.semester')),
            ],
        ),
        migrations.AddField(
            model_name='routine',
            name='related',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='server.routine_head'),
        ),
    ]
