# Generated by Django 5.0.6 on 2024-08-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_teacher_groups_teacher_is_active_teacher_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parentPhone',
            field=models.TextField(max_length=13, verbose_name='Parents Phone no.'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Teacher Phone no.'),
        ),
    ]
