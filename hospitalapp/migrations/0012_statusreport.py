# Generated by Django 5.0.6 on 2024-08-29 18:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0011_remove_notification_is_read_remove_notification_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='statusreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospitalapp.schedule')),
            ],
        ),
    ]
