# Generated by Django 4.0.5 on 2022-12-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0110_alter_routine_options_alter_hod_branch_alter_hod_hod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_discussion',
            name='user_type',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='group_discussion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group_discussion'),
        ),
    ]
