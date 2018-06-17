from django.db import models

# Create your models here.


class PersonalData(models.Model):
	firstName = models.CharField(max_length=120)
	lastName = models.CharField(max_length=120)
	age = models.CharField(max_length=20)
	email = models.CharField(max_length=120)
	occupation = models.CharField(max_length=120)
	status = models.CharField(max_length=120)

	def __str__(self):
		return self.firstName