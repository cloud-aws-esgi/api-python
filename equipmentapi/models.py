# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equipment(models.Model):
    id_equipment = models.AutoField(primary_key=True)
    title = models.TextField()
    id_state = models.ForeignKey('State', models.DO_NOTHING, db_column='id_state', blank=True, null=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Equipment'

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id_equipment, self.title, self.id_state, self.id_user)

class State(models.Model):
    id_state = models.AutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'State'

    def __str__(self):
        return "{} - {}".format(self.id_state, self.title)

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.TextField()
    firstname = models.TextField()
    address = models.CharField(max_length=100)
    mail = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'User'
    
    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.id_user, self.name, self.firstname, self.address, self.mail)
