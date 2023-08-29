from django.contrib import admin

# Register your models here.
from .models import Cart

class CartAdmin(admin.ModelAdmin):
  list_display = [
	'cart_id',
    'p_id',
    'c_id'
  ]

admin.site.register(Cart, CartAdmin)
