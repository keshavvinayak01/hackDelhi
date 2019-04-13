from __future__ import unicode_literals

from django.shortcuts import render

def HomeView(request):
	return render(request,'ed4/home.html') 