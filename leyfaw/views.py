from django.shortcuts import render

from django.http import HttpResponse


def tay(request):
    return HttpResponse("Law, leyvite! Vi ye paygi li tay.")
