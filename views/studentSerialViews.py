from requests import Response
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView
from .serializing import *
from onlineapp.models import *
from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from onlineapp.models import College,Student,MockTest1
from django.utils.six import BytesIO
from django.test import TestCase
from rest_framework.views import APIView
@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = studentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = studentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = studentDetailSerialize(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = studentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

class studentListApi(ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all().filter(college__id=kwargs['college__id'])
        serialize= studentSerializer(queryset,many=True)
        return JsonResponse(serialize.data,safe=False)

class studentDetailsApi(ListAPIView):
    serializer_class = studentDetailSerialize
    def get_queryset(self):
        queryset=Student.objects.all().filter(college__id=self.kwargs.get('college__id')).filter(id=self.kwargs.get('student__id'))
        return queryset

class studentDetailsUpdateApi(UpdateAPIView):
    serializer_class = studentDetailSerialize
    lookup_field = 'pk'
    def get_queryset(self):
        queryset=Student.objects.all()
        return queryset



class studentDetailDeleteApi(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = studentDetailSerialize
    lookup_field = 'pk'

class studentDetailCreateApi(CreateAPIView):

    serializer_class = studentDetailSerialize
    def create(self, request, *args, **kwargs):
        total=int(request.data['mocktest1.problem1'])+int(request.data['mocktest1.problem2'])+int(request.data['mocktest1.problem3'])+int(request.data['mocktest1.problem4'])
        student=Student.objects.create(name=request.data['name'],dob=request.data['dob'],email=request.data['email'],db_folder=request.data['db_folder'],dropped_out=False,college_id=kwargs['college__id'])
        mocktest=MockTest1.objects.create(problem1=request.data['mocktest1.problem1'],problem2=request.data['mocktest1.problem2'],problem3=request.data['mocktest1.problem3'],problem4=request.data['mocktest1.problem4'],total=total,student_id=student.id)
        student.save()
        mocktest.save()
        return HttpResponse("success")

