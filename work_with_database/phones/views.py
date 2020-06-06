from django.shortcuts import render

from .models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort_order = request.GET.get('sort', 'name')
    if sort_order == 'name':
        phones = Phone.objects.order_by("name")
    elif sort_order == 'min_price':
        phones = Phone.objects.order_by("price")
    elif sort_order == 'max_price':
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.order_by("name")

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.get(slug=slug)

    context = {'phone': phone}
    return render(request, template, context)
