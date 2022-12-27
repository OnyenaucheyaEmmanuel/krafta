from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=200,default="Krafta")
	# site_name = models.CharField(max_length=255,default="Krafta")
	# background_colour = models.CharField(max_length=255,default="lemon")
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
# class Name(models.Model):
# 	site_name = models.CharField(max_length=255)
# 	background_colour = models.CharField(max_length=255)