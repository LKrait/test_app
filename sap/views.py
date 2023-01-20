from django.shortcuts import render
from django.contrib.auth import login, logout



def index(request):
	return render(request, "sign-in/index.html")
