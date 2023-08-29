from django.test import TestCase

# Create your tests here.
from core.models import Product

from django.db import connections

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.filter(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user[0].check_password(password):
                return user
        return None

class ProductTest(TestCase):


	def sql(query):
		cursor = connections['default'].cursor()
		cursor.execute(query)
		try:
			rows = cursor.fetchall()
			return rows
		except:
			return []

	print(sql('''
			SELECT *
			FROM cart c, customers cu, products p
			WHERE cu.c_id = c.c_id AND p.p_id = c.p_id AND c.c_id = 1
			'''
	))

	print(sql(f'''
				select * from cart
				WHERE c_id = 1
					''')	)

	print(sql(f'''
				select p_quantity from products
				WHERE p_id = 9
					''')[0][0]	)

	print(sql(f'''
				SELECT o_deliverdate, o_orderdate, o_shipdate, p_id FROM orders
				WHERE c_id = 1
				group by o_shipdate, c_id, p_id, o_deliverdate, o_orderdate , o_shipdate
					''')	)

	#print(EmailBackend.authenticate(username="tymeat39@gmail.com", password="testingtesting")[0])





