from django.db import models

PHENOTYPE_CHOICES = (
	("sativa","Sativa"),
	("hybrid","Hybrid"),
	("indica","Indica"),
)

class Strain(models.Model):
	name = models.CharField(max_length=140)
	pheno = models.CharField(max_length=6, choices=PHENOTYPE_CHOICES, default='hybrid')
	cbd = models.BooleanField(default=0)
	favorite = models.BooleanField(default=0)

	def __str__(self):
		return self.name

class Advanced(models.Model):
	dispensary = models.CharField(max_length=140)
	leafly = models.CharField(max_length=140)
	stats = models.BooleanField(default=0)
	
	def __str__(self):
		return self.dispensary