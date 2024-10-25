from django.http import JsonResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def compiler(request: HttpRequest):
    return JsonResponse({}, status=200, safe=False)