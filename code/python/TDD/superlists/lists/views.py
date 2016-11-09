from django.shortcuts import render
from django.http import HttpResponse

# 在這複創造你的 view
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST['item_text'],
    })
