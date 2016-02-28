# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-28 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serves_hot_dogs', models.BooleanField(default=True)),
                ('serves_pizzas', models.BooleanField(default=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_changed', models.DateTimeField(auto_now=True)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_changed', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Restaurant')),
            ],
        ),
    ]
