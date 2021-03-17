from django.shortcuts import render
from .models import Product


def productlist(request):
    productlist = Product.objects.all()
    print(productlist)
    context = {'product_list': productlist}
    template = 'Product/product_list.html'

    return render(request, template, context)


def productdetail(request, id):
    print(id)
    productdetail = Product.objects.get(id=id)
    template = 'Product/product_detail.html'
    context = {'product_detail': productdetail}
    return render(request, template, context)
