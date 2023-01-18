from django.shortcuts import render



def index(request):
	return render(request, "sign-in/index.html")
