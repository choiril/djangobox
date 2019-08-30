from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	judul = models.CharField(max_length=200)
	isi = models.TextField()
	tgl_buat = models.DateTimeField(default=timezone.now)
	tgl_terbit = models.DateTimeField(blank=True, null=True)
	
	def terbit(self):
		self.tgl_terbit = timezone.now()
		self.save()
	
	def __str__(self):
		return self.judul
