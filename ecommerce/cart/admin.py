from django.contrib import admin
from cart.models import Cart,Account,Order
from django.http import HttpResponse
admin.site.register(Cart)s
admin.site.register(Account)
admin.site.register(Order)
