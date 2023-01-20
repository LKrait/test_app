from django.shortcuts import render
from django.contrib.auth import login, logout


def index(request):
	return render(request, "index.html")


def home(request):
	return render(request, "dashboard/index.html",{})
