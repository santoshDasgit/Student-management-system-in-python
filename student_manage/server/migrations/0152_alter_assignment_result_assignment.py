# Generated by Django 4.0.5 on 2022-12-29 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0151_alter_assignment_submit_student_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_result',
            name='assignment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment_result', to='server.assignment_submit_student'),
        ),
    ]
