# Generated by Django 5.1 on 2024-08-08 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_alter_student_teacher_alter_teacher_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='onboarded',
        ),
    ]
