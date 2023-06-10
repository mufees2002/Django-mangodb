from django.shortcuts import render
from django.http import HttpResponse
from .models import Info
from .serilizers import InfoSerilizers
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
@api_view(['GET','POST','DELETE'])
def SaveInfo(request):
    Info_DB=JSONParser().parse(request)
    Info_Serilizer=InfoSerilizers(data=Info_DB)
    if Info_Serilizer.is_valid():
        Info_Serilizer.save()
        return JsonResponse(Info_Serilizer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(Info_Serilizer.errors, status=status.HTTP_400_BAD_REQUEST)