from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

@login_required
def index_view(request):
    return HttpResponse('index')

@login_required
def batch_view(request):
    return HttpResponse('batch')

@login_required
def snps_view(request):
    return HttpResponse('snps')

@login_required
def upload_view(request):
    return HttpResponse('uploads')
