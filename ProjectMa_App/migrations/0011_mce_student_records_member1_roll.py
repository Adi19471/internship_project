# Generated by Django 3.2.7 on 2021-09-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectMa_App', '0010_auto_20210924_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='mce_student_records',
            name='Member1_Roll',
            field=models.IntegerField(default=False),
        ),
    ]