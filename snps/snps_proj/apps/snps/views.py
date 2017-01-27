from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index_view(request):
    return HttpResponse('index')


def batch_view(request):
    return HttpResponse('batch')


def snps_view(request):
    return HttpResponse('snps')


def upload_view(request):
    return HttpResponse('uploads')
