from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print("in index")
    return render(request, "language_reference/index.html")

def hello_world(request):
    print("in hello")
    return render(request, "language_reference/hello-world.html")