from django.shortcuts import render,redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort_by = request.GET.get('sort')

    phones = Phone.objects.all()


    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'min_price':
        phones = phones.order_by('price')
    elif sort_by == 'max_price':
        phones = phones.order_by('-price')

    template = 'catalog.html'
    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)

