from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from allauth.account.forms import LoginForm, SignupForm

def login(request):
    context = {
        'login_form': LoginForm()
    }
    return render(request, 'login.html', context)

@login_required
def index_view(request):
    return render(request, 'index.html', {})

@login_required
def batch_view(request):
    return render(request, 'batches.html', {})

@login_required
def snps_view(request):
    return render(request, 'snps.html', {})

@login_required
def upload_view(request):
    return render(request, 'upload.html', {})
