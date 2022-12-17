from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    products =  Product.objects.all()
    return render(request,'market/index.html', {'products':products})

def create(request):
    if request.method == 'POST':
        productForm = ProductForm(request.POST)

        if productForm.is_valid():
            productForm.save()

            return HttpResponseRedirect('/market/')
    
    else:
        productForm = ProductForm()
    
    return render(request, 'market/create.html', {'productForm':productForm})

def find(request,slug):
    product = Product.objects.get(id=slug)
    return render(request, 'market/product.html', {'product':product})

def delete(request,slug):
    product = get_object_or_404(Product, id=slug)

    if request.method == "POST":
        product.delete()
        return HttpResponseRedirect('/market/')

    return render(request, "market/delete.html")

def edit(request,slug):
    product = get_object_or_404(Product, id=slug)
    productForm = ProductForm(request.POST or None, instance=product)

    if productForm.is_valid():
        productForm.save()
        return HttpResponseRedirect('/market/'+slug)

    return render(request, 'market/edit.html', {'productForm':productForm, 'productId':slug})