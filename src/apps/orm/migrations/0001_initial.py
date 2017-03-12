# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.CharField(max_length=255)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.CharField(max_length=255)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('content', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.CharField(max_length=255)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('label', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('is_private', models.BooleanField(default=False)),
                ('is_anonymous', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRoomRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.CharField(max_length=255)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('handle_name', models.CharField(max_length=255)),
                ('role', models.PositiveSmallIntegerField(choices=[('RWX', 0), ('RW', 1), ('R', 2)], default='RW')),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]