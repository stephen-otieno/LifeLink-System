# Generated by Django 5.1.3 on 2025-03-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LifeLinkApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filled_at', models.DateTimeField(auto_now_add=True)),
                ('recipient_name', models.CharField(max_length=100)),
                ('recipient_bloodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=3)),
                ('recipient_contact', models.CharField(max_length=50)),
                ('recipient_address', models.CharField(max_length=50)),
            ],
        ),
    ]
