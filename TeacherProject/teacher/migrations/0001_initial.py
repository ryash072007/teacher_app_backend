# Generated by Django 5.1 on 2024-08-07 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Teacher Email Address')),
                ('password', models.TextField(max_length=20, verbose_name='Teacher Password')),
                ('phone', models.IntegerField(max_length=10, verbose_name='Teacher Phone no.')),
                ('name', models.TextField(max_length=30, verbose_name='Teacher Name')),
                ('qualifications', models.TextField(blank=True, max_length=200, verbose_name='Teacher Qualifications')),
                ('onboarded', models.BooleanField(default=False, verbose_name='Teacher Onboarded Status')),
                ('forgottenPassword', models.BooleanField(default=False, verbose_name='Teacher Forgotten Password')),
                ('otp', models.IntegerField(blank=True, max_length=4, null=True, verbose_name='OTP Password')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField(max_length=30, verbose_name='Student First Name')),
                ('lastName', models.TextField(max_length=30, verbose_name='Student Last Name')),
                ('gender', models.TextField(choices=[('male', 'Male'), ('female', 'Female')], verbose_name='Student Gender')),
                ('grade', models.IntegerField(max_length=2, verbose_name='Student Grade')),
                ('studentDesc', models.TextField(blank=True, max_length=200, verbose_name='Student Description')),
                ('displayImage', models.ImageField(upload_to='', verbose_name='Student Display Image')),
                ('parentName', models.TextField(max_length=30, verbose_name='Parents Name')),
                ('parentEmail', models.EmailField(max_length=50, verbose_name='Parents Email Address')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
