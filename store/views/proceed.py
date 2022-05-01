from django.shortcuts import render , redirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order

class Proceed(View):

    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        total=0
        for order in orders:
            total+=order.quantity*order.price
        return render(request,'proceed.html', {'total':total})

