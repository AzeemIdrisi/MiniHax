from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req, "webpages/home.html")


def login(req):
    return render(req, "webpages/login.html")


def signup(req):
    return render(req, "webpages/signup.html")


def dashboard(req):
    return render(req, "webpages/dashboard.html")


def details(req, id):
    print(id)
    if id == "1":
        return render(req, "webpages/caseDetails1.html")
    else:
        return render(req, "webpages/signup.html")
