from django.contrib import admin

# Register your models here.
from .models import Customer, Order, Product

class ProductAdmin(admin.ModelAdmin):
  list_display = [
    'p_id',
    'p_name',
    'p_brand',
    'p_description',
	  'p_imgurl',
	  'p_price',
	  'p_quantity'
  ]

class CustomerAdmin(admin.ModelAdmin):
  list_display = [
    'c_id',
    'c_address',
    'c_name',
	'c_email',
	'c_money_spent',
  ]

class OrderAdmin(admin.ModelAdmin):
  list_display = [
    'o_num_items',
    'c_id',
    'p_id',
	'o_shipdate',
	'o_deliverdate',
	'o_id'
  ]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)