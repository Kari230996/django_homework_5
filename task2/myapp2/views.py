from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Order, Product
from .crud import get_all_clients, get_all_products
from datetime import timedelta
from .forms import ProductForm


# Create your views here.

def home(request):
    return render(request, 'myapp2/home.html')

def display_data(request):
    clients = get_all_clients()
    products = get_all_products()

    return render(request, 'myapp2/data_display.html', {'clients': clients, 'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
   
    return render(request, 'myapp2/product_detail.html', {'product': product})

def orders_list_view(request):
    orders = Order.objects.all()
    return render(request, 'myapp2/orders_list.html', {'orders': orders})



def ordered_product_list(request):
    today = timezone.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)

    ordered_product_last_week = get_ordered_products(last_week, today)
    ordered_product_last_month = get_ordered_products(last_month, today)
    ordered_product_last_year = get_ordered_products(last_year, today)

    return render(request, 'myapp2/ordered_products_list.html', {
        'ordered_product_last_week': ordered_product_last_week,
        'ordered_product_last_month': ordered_product_last_month,
        'ordered_product_last_year': ordered_product_last_year
    })



def get_ordered_products(start_date, end_date):
    orders = Order.objects.filter(order_date__range=(start_date, end_date))
    ordered_products = set()

    for order in orders:
        ordered_products.update(order.products.all())

    return ordered_products

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp2/edit_product.html', {'form': form})