from django.db import models

# Create your models here.

class Cart(models.Model):
	cart_id = models.IntegerField(primary_key=True)
	p_id = models.IntegerField()
	c_id = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'cart'


