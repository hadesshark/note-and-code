from django.shortcuts import render
from django.http import HttpResponse

# 在這複創造你的 view
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
