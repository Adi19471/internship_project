# Generated by Django 3.2.7 on 2021-09-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectMa_App', '0011_mce_student_records_member1_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='mce_student_records',
            name='Member2_Roll',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='mce_student_records',
            name='Member3_Roll',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='mce_student_records',
            name='Member4_Roll',
            field=models.IntegerField(default=False),
        ),
    ]
