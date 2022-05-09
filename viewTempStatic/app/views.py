 
from django.shortcuts import render
from django.http import HttpResponse

 
def home(request):
    print(request.COOKIES)
    return HttpResponse("<h1> Hello World </h1>")

def blog(request):
#student = Students.objects.all()

    context={

    "isim": "halil  ",
    "lastname":"kara",
    "dict-1":{"django":"bestframework"},
    "my_list":[1,2,3,4],
}

    return render(request, 'app/index.html', context)