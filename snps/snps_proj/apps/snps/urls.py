"""snps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

import apps.snps.views as views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),

    url(r'upload', views.upload_view, name='upload'),

    url(r'^batch', views.batch_view, name='batch'),
    url(r'^snps', views.snps_view, name='snps'),
    url(r'^login', views.login, name='account_login')
]
