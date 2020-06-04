from django.db import models

# Create your models here.

import datetime
from django.utils import timezone
from django.utils.timezone import now
# Create your models here.

class Member(models.Model):
	ok = models.CharField(max_length=10)
	# members = models.CharField(max_length=100)


class User(models.Model):
	# activity_periods = models.ForeignKey('Activity',on_delete =models.CASCADE)
	members = models.ForeignKey(Member,related_name='members',on_delete=models.CASCADE)
	ids = models.CharField(max_length=40)
	real_name = models.CharField(max_length=40)
	tz = models.CharField(max_length=50)

	class Meta:
		unique_together = ['members','ids']
		ordering =['ids']


	def __str__(self):
		return self.real_name

class Activity(models.Model):
	activity_periods = models.ForeignKey(User,related_name='activity_periods',on_delete=models.CASCADE)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(auto_now=True)



	def __str__(self):
		return str(self.start_date) 

	def __str__(self):
		return str(self.end_date) 


