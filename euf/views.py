from django.shortcuts import redirect, render


def home(req):
    return render(req, "frontend/home.html")
