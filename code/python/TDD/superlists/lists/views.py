from django.shortcuts import render
from django.http import HttpResponse

# 在這複創造你的 view
def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')
