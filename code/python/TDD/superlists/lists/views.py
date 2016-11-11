from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item

# 在這複創造你的 view
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'item': items})
