from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
	if request.method == "GET":
		extra_data = ["SomeExtraData", 123, 1.1]
		if "password" in request.GET.keys():
			if request.GET['password'] == "supersecretpassword":
				return render(request, "home.html", {'username': "priyam", 'abcd': extra_data})
			else:
				return render(request, "home.html", {'username': "wrong", 'abcd': extra_data})
		else:
			return render(request, "home.html", {'abcd': extra_data, 'username': "unknown"})

	elif request.method == "POST":
		print("POST parameters: " + str(request.POST))
		return redirect("/homepage/")

	else:
		msg = "not suppported method"
		return HttpResponse(msg)