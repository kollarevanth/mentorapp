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

class collegeListApi(ListAPIView):
    queryset = College.objects.all()
    serializer_class = collegeSerializer
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = collegeSerializer(queryset, many=True)
    #     return Response(serializer.data[0])

class updateCollegeSerializer(UpdateAPIView):
    queryset = College.objects.all()
    lookup_field = 'name'
    serializer_class = collegeSerializer

class deleteCollegeSerializer(DestroyAPIView):
    queryset = College.objects.all()
    serializer_class = collegeSerializer
    lookup_field = 'name'

class createCollegeSerializer(CreateAPIView):
    queryset = College.objects.all()
    serializer_class = collegeSerializer



@csrf_exempt
def college_list(request):
    if request.method == 'GET':
        snippets = College.objects.all()
        serializer = collegeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = collegeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def college_detail(request, pk):
    try:
        snippet = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = collegeSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = collegeSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)












