# Generated by Django 5.1 on 2024-08-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_teacher_otpverified'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parentPhone',
            field=models.TextField(default=0, max_length=10, verbose_name='Parents Phone no.'),
            preserve_default=False,
        ),
    ]
