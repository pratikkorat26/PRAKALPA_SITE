from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    html = "<html><body>It is now</body></html>"
    return HttpResponse(html)