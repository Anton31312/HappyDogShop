from django.shortcuts import render
from catalog import models

def home_page(request):
    product_list = models.Product.objects.all()
    
    context = {
        "object_list" : product_list,
        'title' : 'Главная'
    }

    return render(request, 'catalog/home.html', context)

def contact_page(request):

    context = {
        'title' : 'Контакты'
    }

    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({phone}, {email}): {message}')

    return render(request, 'catalog/contact.html', context)

def product_info(request, pk):
    context = {
        'object': models.Product.objects.get(pk=pk),
        'title' : 'Продукт'
        }
    
    return render(request, 'catalog/product_info.html', context)