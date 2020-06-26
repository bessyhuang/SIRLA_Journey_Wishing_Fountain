"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from home import datahandler, views


urlpatterns = [
	path('datahandler', datahandler.getdata),
    path('', views.chart, name='chart'),
]