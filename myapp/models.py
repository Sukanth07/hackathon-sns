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
