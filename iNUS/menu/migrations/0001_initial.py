# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MC', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=3)),
                ('module', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='modules',
            name='module_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Sem'),
        ),
    ]
