from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('这是第一个视图')
    return HttpResponse("ok")


def user_log(request):
    pass
    return HttpResponse('1')