from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html"),

def contact(request):
    return render(request, "con.html"),

def service(request):
    return render(request, "serve.html"),

def element(request):
    return render(request, "ele.html"),

def post(request):
    return render(request, "post.html"),