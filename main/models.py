from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Persons(models.Model):
    person_id = models.AutoField(primary_key=True, blank=True)
    master_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    ctc = models.IntegerField(blank=True, null=True)
    cts = models.IntegerField(blank=True, null=True)
    ttc = models.FloatField(blank=True, null=True)
    tts = models.FloatField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Urls(models.Model):
    url = models.TextField(primary_key=True, blank=True)
    unique_clicks = models.IntegerField(blank=True, null=True)
    total_clicks = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    pbc = models.IntegerField(blank=True, null=True)
    pbs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urls'