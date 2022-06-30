from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import blog

# Create your views here.

# def hewo(request):
#    return render(request,"home.html", {'name':'am ginto g thomas'})

     # staticaly import datas this is not a professional way to import data (edu avodha)

# def hewo(request):
#     obj=place()
#     obj.name="kerala"                   #THIS FOR change filed in a template staticly this not right way to change fields
#     obj.price=100
#     obj.desc="gods own country"
#     return render(request,"index.html",{'result':obj})



#dynamicalu=y import or display data (right way) so the admin can easily add data to the sites



# def fun(request):
#     obj=place.objects.all( )
#     return render(request,"index.html",{'results':obj})
#
# def func(request):
#     obj=blog.objects.all( )
#     return render(request,"index.html",{'blogresults':obj})

def fun(request):
    obj_0=place.objects.all()
    obj_1=blog.objects.all()
    return render(request,"index.html",{'results':obj_0,'blogresults':obj_1})

# def addtwo(request):
#     num1=int(request.POST["num1"])
#     num2=int(request.POST["num2"])
#     num3=num1+num2
#     return render(request,"resultof2.html",{'add':num3})



