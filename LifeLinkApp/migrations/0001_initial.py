# Generated by Django 5.1.3 on 2025-03-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filled_at', models.DateTimeField(auto_now_add=True)),
                ('donor_name', models.CharField(max_length=100)),
                ('donor_bloodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=3)),
                ('donor_contact', models.CharField(max_length=50)),
                ('donor_address', models.CharField(max_length=50)),
            ],
        ),
    ]
