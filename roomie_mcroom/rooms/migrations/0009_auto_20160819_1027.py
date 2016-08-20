# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0008_bookingsociety'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society_name', models.CharField(max_length=100)),
                ('user_model', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bookingsociety',
            name='id',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='bookingsociety',
            name='booking_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bookingsociety',
            name='society',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Society'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='associated_society',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='associated_society',
            field=models.ManyToManyField(blank=True, to='rooms.Society'),
        ),
    ]
