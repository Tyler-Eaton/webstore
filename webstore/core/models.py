from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

# products table model
class Product(models.Model):
	p_id = models.IntegerField(primary_key=True)
	p_name = models.CharField(max_length=25)
	p_brand = models.CharField(max_length=25)
	p_description = models.CharField(max_length=152, null=True, blank=True)
	p_imgurl = models.CharField(max_length=500, null=True, blank=True)
	p_price = models.DecimalField(max_digits=15, decimal_places=2)
	p_quantity = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'products'

	def __str__(self):
		return self.p_name

# order table model
class Order(models.Model):
	o_id = models.IntegerField(primary_key=True)
	o_num_items = models.IntegerField(validators=[MinValueValidator(1)])
	c_id = models.IntegerField()
	p_id = models.IntegerField()
	o_shipdate = models.DateField()
	o_deliverdate = models.DateField()
	o_orderdate = models.DateField()

	class Meta:
		managed = False
		db_table = 'orders'

	def __str__(self):
		return f"Order {self.p_id}"

# customer table model
class Customer(models.Model):
	c_id = models.IntegerField(primary_key=True)
	c_address = models.CharField(max_length=40)
	c_name = models.CharField(max_length=25)
	c_email = models.EmailField(max_length=40)
	c_money_spent = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'customers'

	def __str__(self):
		return self.c_name

