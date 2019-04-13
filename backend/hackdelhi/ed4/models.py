# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def custom_directory_path(instance,filename):
	return 'files/{0}/{1}'.format(word2video.objects.all().count() + 1,filename)

class word2video(models.Model):
	document = models.FileField(upload_to=custom_directory_path, blank=True)
	text = models.TextField(max_length = 2000,blank=True)
	video = models.FileField(upload_to=custom_directory_path, blank=True)

	class Meta:
		ordering = ["-id"]

	def __str__(self):
		return str(self.id)