from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'storage/index.html')
def pool(request):
    print "this is pool method"
    return render(request,'storage/pool.html')
def makepool(request):
    
    print "this is a all method"
    if request.method=="POST":
        print "this is post method"
        print "get data here"
        return render(request,"storage/pool.html")
    else:
        print "this is get  method"
        return render(request,"storage/makepool.html")
        
