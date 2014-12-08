from django.db import models
from django.contrib import admin

class UserInfo(models.Model):
	username = models.CharField(max_length=20)
	birthday = models.DateTimeField()
	hometown = models.CharField(max_length=20)
	describ = models.CharField(max_length=200)
	def __unicode__(self):
	    return self.username
admin.site.register(UserInfo)