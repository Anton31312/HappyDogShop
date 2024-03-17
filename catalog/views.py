from django.shortcuts import render

def home_page(request):
    return render(request, 'catalog/home.html')

def contact_page(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({phone}, {email}): {message}')
    return render(request, 'catalog/contact.html')
