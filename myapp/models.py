from django.db import models

# Django models correspond to table definitions in the database.
# For example, the Person table will have columns:
# first_name, last_name, address, tel, email

# Usually, all interaction with the database in Django is through
# these objects (rather than using another database API or writing
# SQL)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel = models.CharField(max_length=18)
    email = models.CharField(max_length=50)

class Business(models.Model):
    business_name = models.CharField(max_length=60)
    tel = models.CharField(max_length=18)
    email = models.CharField(max_length=50)
