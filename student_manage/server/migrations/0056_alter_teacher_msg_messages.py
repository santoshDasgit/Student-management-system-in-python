# Generated by Django 4.0.5 on 2022-10-30 19:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0055_alter_teacher_msg_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_msg',
            name='messages',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
