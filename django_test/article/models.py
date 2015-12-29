from django.db import models
from time import time

def get_upload_file_name(instance,filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

class Article(models.Model):
	title = models.CharField(max_length = 200)
	tags = models.CharField(max_length = 200)
	body = models.TextField()
	
	def __str__(self):
		return self.title

