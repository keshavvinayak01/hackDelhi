# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class word_to_text(models.Model):
	document = models.FileField()s
	text = models.TextField(max_length = 2000)
	