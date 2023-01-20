# Generated by Django 4.0.5 on 2022-11-10 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0076_studentsfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='server.session_year')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='server.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_chields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.attendance')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.student')),
            ],
        ),
    ]
