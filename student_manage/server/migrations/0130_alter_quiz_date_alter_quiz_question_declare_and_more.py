# Generated by Django 4.0.5 on 2022-12-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0129_quiz_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_declare',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='result_declare',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
