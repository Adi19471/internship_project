# Generated by Django 3.2.7 on 2021-09-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectMa_App', '0002_alter_semester_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCE_CSE_Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
