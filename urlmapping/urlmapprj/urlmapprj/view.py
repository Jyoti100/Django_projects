from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def helllo(request):
	return HttpResponse('This is Http GET request')
