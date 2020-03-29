from django.db import models

class participants(models.Model):
	fullname = models.CharField(max_length=40)
	emailid = models.CharField(max_length=40, unique=True)
	rollno = models.CharField(max_length=4, unique=True)
	team = models.CharField(max_length=1)
	username = models.CharField(max_length=20, unique=True)
	username2 = models.CharField(max_length=20, default="TEST")