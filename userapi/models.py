# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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