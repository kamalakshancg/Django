from django.db import models

from django.urls import reverse
# Create your models here.

class Student(models.Model):
	Name = models.CharField(max_length=30)
	Number=models.IntegerField()
	Marks = models.FloatField()
	Address=models.CharField(max_length=30)

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse("detail",kwargs={'pk':self.pk})