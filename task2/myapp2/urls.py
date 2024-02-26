from django.urls import path
from .views import product_detail, edit_product, display_data, orders_list_view, ordered_product_list, home
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home, name='home'),
    path('display-data/', display_data, name='display_data'),
    path('orders/', orders_list_view, name='orders_list'),
    path('ordered-products/', ordered_product_list, name='ordered_product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/<int:product_id>/edit/', edit_product, name='edit_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)