# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0031_auto_20171118_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='Department',
            field=models.CharField(blank=True, choices=[('Biosciences_and_Bioengineering', 'Biosciences and Bioengineering'), ('Chemical_Engineering', ' Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Computer_Science_and_Engineering', 'Computer Science and Engineering'), ('Civil_Engineering', 'Civil Engineering'), ('Design', 'Design'), ('Humanity_and_Social_Sciences', 'Humanity and Social Sciences'), ('Electronics_and_Electrical_Engineering ', ' Electronics and Electrical Engineering '), ('Mathematics', 'Mathematics'), ('Mechanical_Engineering', 'Mechanical Engineering'), ('Physics', 'Physics')], default=None, max_length=200, null=True),
        ),
    ]
