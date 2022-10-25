from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render())


def email(request):
    temp = loader.get_template('email.html')
    return HttpResponse(temp.render())


def edu(request):
    temp = loader.get_template('edu.html')
    return HttpResponse(temp.render())


def course(request):
    temp = loader.get_template('course.html')
    return HttpResponse(temp.render())


def last(request):
    temp = loader.get_template('last.html')
    return HttpResponse(temp.render())


