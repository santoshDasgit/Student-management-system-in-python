# Generated by Django 4.1.2 on 2022-11-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0070_alter_teacher_leave_apply_end_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('course', 'branch')},
        ),
    ]
