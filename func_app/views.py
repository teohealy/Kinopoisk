from django.shortcuts import render
from django.http import HttpResponse
import summary


def index(request, ):
    a = summary.summary('/app/kinopoisk.html')
    return HttpResponse('<br>'.join(a))


