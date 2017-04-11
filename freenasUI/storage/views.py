from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'storage/index.html')
def pool(request):
    return render(request,'storage/pool.html')
