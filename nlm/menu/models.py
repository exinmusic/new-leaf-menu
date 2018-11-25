from django.db import models

PHENOTYPE_CHOICES = (
	("sativa","Sativa"),
	("hybrid","Hybrid"),
	("indica","Indica"),
)

class Strain(models.Model):
	name = models.CharField(max_length=140)
	pheno = models.CharField(max_length=6, choices=PHENOTYPE_CHOICES)
	cbd = models.BooleanField()
	favorite = models.BooleanField()

	def __str__(self):
		return self.name
