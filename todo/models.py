from django.db import models

class Tarea(models.Model):
	tarea = models.CharField(max_length=100)
	dia = models.CharField(max_length=50)
	acciones=models.CharField(max_length=100)
	


	def __str__(self):
		return self.tarea







