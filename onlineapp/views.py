from django.shortcuts import render
from django.http import HttpResponse
from onlineapp.models import *
from django.template import loader

def hello(request):
    fp=open("onlineapp/testing.html","r")
    li=fp.readlines()
    s=''.join(li)
    return HttpResponse(s)
# def print_college_names(request):
#     reqhtml=College.objects.values_list('name')
#
#     li=[list(x) for x in reqhtml]
#     reqhtml=''.join(str(li))
#
#     stri="<html><body>"+reqhtml+"</body></html>"
#     return HttpResponse(stri)


def print_college_names(request):
    reghtml=College.objects.values_list('name','acronym')
    template=loader.get_template('testing.html')
    print(reghtml)
    reghtml=[[i[0],i[1]] for i in reghtml]
    context={'clist':reghtml}
    return render(request,'testing.html',context)

def print_student_details_acronym(request,value):
    result_set=Student.objects.values('name','email','college__acronym').get(id=value)
    result_set=[result_set]
    print(result_set)
    template=loader.get_template('studentDetailsAndAcronym.html')
    context={'resList':result_set}
    return render(request,'studentDetailsAndAcronym.html',context)

def test_http_request(request):
    request.session.setdefault("Counter",0)
    count=request.session["Counter"]+1
    request.session["Counter"]=count
    return HttpResponse("It has called{}".format(count))

def test_exception(request):
    raise ValueError()















