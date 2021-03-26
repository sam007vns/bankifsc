from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class BankNames(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
    	return self.name
    def get_absolute_url(self):
    	return reverse('select_bank_',args=[str(self.name.replace(" ","_"))])
    class Meta:
        managed = False
        db_table = 'Bank_Names'


class Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    ifsc = models.CharField(max_length=100, blank=True, null=True)
    adr1 = models.TextField(blank=True, null=True)
    adr2 = models.TextField(blank=True, null=True)
    adr3 = models.TextField(blank=True, null=True)
    adr4 = models.TextField(blank=True, null=True)
    adr5 = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    micr = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
    	return self.name
    class Meta:
        managed = False
        db_table = 'data'