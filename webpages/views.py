from django.shortcuts import render, redirect


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
    if id == 1:
        return render(req, "webpages/caseInformation.html")
    if id == 2:
        return render(req, "webpages/quantitative.html")
    if id == 3:
        return render(req, "webpages/qualitative.html")
    if id == 0:
        return redirect("dashboard")
    else:
        return render(req, "webpages/signup.html")


def schedule(req, id):
    if id == 1:
        return render(req, "webpages/schedule1.html")
    if id == 2:
        return render(req, "webpages/schedule2.html")
    else:
        return render(req, "webpages/schedule3.html")
