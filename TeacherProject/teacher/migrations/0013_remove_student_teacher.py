# Generated by Django 5.0.6 on 2024-08-13 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_alter_student_parentphone_alter_teacher_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
