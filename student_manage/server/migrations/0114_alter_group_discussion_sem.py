# Generated by Django 4.0.5 on 2022-12-05 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0113_rename_branch_group_discussion_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_discussion',
            name='sem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.semester'),
        ),
    ]
