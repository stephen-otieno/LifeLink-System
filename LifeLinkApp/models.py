from django.db import models

class Donor(models.Model):
    filled_at=models.DateTimeField(auto_now_add=True)
    donor_name = models.CharField(max_length=100)

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    donor_bloodGroup = models.CharField(max_length=3, choices= BLOOD_GROUP_CHOICES, default='O+')
    donor_contact = models.CharField(max_length=50)
    donor_address = models.CharField(max_length=50)

    def __str__(self):
        return self.donor_name

class Recipient(models.Model):
    filled_at=models.DateTimeField(auto_now_add=True)
    recipient_name = models.CharField(max_length=100)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    recipient_bloodGroup = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default='O+')
    recipient_contact = models.CharField(max_length=50)
    recipient_address = models.CharField(max_length=50)
    recipient_message = models.TextField(max_length=500)

    def __str__(self):
        return self.recipient_name


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    client_message = models.TextField(max_length=500)
    filled_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class OrganDonor(models.Model):
    filled_at = models.DateTimeField(auto_now_add=True)
    donor_name = models.CharField(max_length=100)

    ORGAN_TYPE_CHOICES = [
        ('Kidney', 'Kidney'),
        ('Heart', 'Heart'),
        ('Lung', 'Lung'),
        ('Liver', 'Liver'),
        ('Pancreas', 'Pancreas'),
        ('Heart Valve', 'Heart Valve'),

    ]

    donor_organType = models.CharField(max_length=20, choices=ORGAN_TYPE_CHOICES, default='Kidney')
    donor_contact = models.CharField(max_length=50)
    donor_address = models.CharField(max_length=50)

    def __str__(self):
        return self.donor_name

class OrganRecipient(models.Model):
    filled_at = models.DateTimeField(auto_now_add=True)
    recipient_name = models.CharField(max_length=100)

    ORGAN_TYPE_CHOICES = [
        ('Kidney', 'Kidney'),
        ('Heart', 'Heart'),
        ('Lung', 'Lung'),
        ('Liver', 'Liver'),
        ('Pancreas', 'Pancreas'),
        ('Heart Valve', 'Heart Valve'),

    ]

    recipient_organType = models.CharField(max_length=20, choices=ORGAN_TYPE_CHOICES, default='Kidney')
    recipient_contact = models.CharField(max_length=50)
    recipient_address = models.CharField(max_length=50)
    recipient_message = models.TextField(max_length=500)

    def __str__(self):
        return self.recipient_name



# Create your models here.
