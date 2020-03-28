from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	if request.method == "GET":
		msg = "YEAH !! A user just opened your website"
		print(msg)
	elif request.method == "POST":
		msg = "YEAH !! A user just sent some data to your website"
		print(msg)
	else:
		msg = "not suppported method"
		print(msg)
	return HttpResponse(msg)