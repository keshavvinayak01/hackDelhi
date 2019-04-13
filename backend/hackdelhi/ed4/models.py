# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def custom_directory_path(instance,filename):
	return 'profilepics/{0}/{1}'.format(instance._id,filename)

class word_to_text(models.Model):
	document = models.FileField(upload_to='custom_directory_path', blank=True)
	text = models.TextField(max_length = 2000,blank=True)
    video = models.FileField(upload_to='custom_directory_path', blank=True)
    
    class Meta:
        ordering = ["-_id"]

    def __str__(self):
    	return self._id