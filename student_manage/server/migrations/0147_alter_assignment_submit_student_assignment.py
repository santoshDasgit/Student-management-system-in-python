# Generated by Django 4.0.5 on 2022-12-28 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0146_assignment_assignment_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_submit_student',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.assignment'),
        ),
    ]
