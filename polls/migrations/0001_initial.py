# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adequacy', models.IntegerField(default=1)),
                ('timestart', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textQuestion', models.CharField(max_length=1000)),
                ('normalQuestion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='questionid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
        ),
    ]
