# Generated by Django 4.1.2 on 2022-10-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_alter_student_father_ph_alter_student_mother_ph'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ph',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
