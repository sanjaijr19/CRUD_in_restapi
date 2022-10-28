"""djrestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter,SimpleRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]


