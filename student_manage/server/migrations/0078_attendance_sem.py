# Generated by Django 4.1.2 on 2022-11-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0077_attendance_attendance_chields'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='sem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.semester'),
        ),
    ]
