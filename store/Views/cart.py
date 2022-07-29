from django.shortcuts import render
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):

        ids_list = list(request.session.get('cart').keys())

        product= Product.get_products_by_id(ids_list)
        print(product)
        return render(request, 'cart.html', {'products': product})

