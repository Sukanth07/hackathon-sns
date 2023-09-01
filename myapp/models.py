from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    graduation = models.CharField(max_length=10)

    class Meta:
        managed = False  # This prevents Django from trying to manage the table
        db_table = 'Users'  # Specify the actual table name in your database

class CLT(models.Model):
    username = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    prize_won = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'clt'
        
class SCD(models.Model):
    username = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    prize_won = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'scd'
        
class CFC(models.Model):
    username = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    
    class Meta:
        managed = False
        db_table = 'cfc'
        
class IIPC(models.Model):
    username = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    
    class Meta:
        managed = False
        db_table = 'iipc'
        
class SRI(models.Model):
    username = models.CharField(max_length=100)
    club = models.CharField(max_length=100)

    
    class Meta:
        managed = False
        db_table = 'sri'