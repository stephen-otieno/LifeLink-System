# Generated by Django 5.1.3 on 2025-03-10 01:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LifeLinkApp', '0002_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='recipient_message',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
