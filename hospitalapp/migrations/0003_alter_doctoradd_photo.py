# Generated by Django 5.0.6 on 2024-07-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_alter_login_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoradd',
            name='photo',
            field=models.CharField(max_length=100),
        ),
    ]
