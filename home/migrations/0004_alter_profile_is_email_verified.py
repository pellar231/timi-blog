# Generated by Django 5.1 on 2024-09-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blogmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_email_verified',
            field=models.BooleanField(default=True),
        ),
    ]
