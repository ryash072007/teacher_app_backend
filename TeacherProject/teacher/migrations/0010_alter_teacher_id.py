# Generated by Django 5.0.6 on 2024-08-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_student_parentphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Teacher ID'),
        ),
    ]
