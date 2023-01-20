# Generated by Django 4.0.5 on 2022-10-30 19:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0056_alter_teacher_msg_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_msg',
            name='messages',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher_msg',
            name='teacher',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='server.teacher'),
        ),
    ]
