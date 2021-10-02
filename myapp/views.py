from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    x = {'name' : 'Ahmed Sameh Ahmed Almisalamy' , 'age' : 16}
    return render(request , "pages/index.html" , x)

def home(request):
    pass

def about(request):
    return render(request, 'pages/about.html')