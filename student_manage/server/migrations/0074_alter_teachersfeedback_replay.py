# Generated by Django 4.1.2 on 2022-11-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0073_teachersfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersfeedback',
            name='replay',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
