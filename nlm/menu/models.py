from django.db import models

class Strain(models.Model):
	name = models.CharField(max_length=140)
	thc = models.IntegerField()
	cbd = models.IntegerField()

	def __str__(self):
		return self.title
