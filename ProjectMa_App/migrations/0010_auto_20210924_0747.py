# Generated by Django 3.2.7 on 2021-09-24 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectMa_App', '0009_auto_20210923_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mce_student_records',
            name='Member2_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mce_student_records',
            name='Member3_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mce_student_records',
            name='Member4_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
