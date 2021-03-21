from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count

def productlist(request):
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))

    paginator = Paginator(productlist, 1)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {'product_list': productlist, 'category_list': categorylist}
    template = 'Product/product_list.html'

    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    product_images = ProductImages.objects.filter(product=productdetail)
    template = 'Product/product_detail.html'
    context = {'product_detail': productdetail, 'product_images': product_images}
    return render(request, template, context)
