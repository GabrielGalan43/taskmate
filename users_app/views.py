from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse('users_app working')