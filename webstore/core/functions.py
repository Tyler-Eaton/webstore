from django.db import connections

def sql(query):
		cursor = connections['default'].cursor()
		cursor.execute(query)
		try:
			rows = cursor.fetchall()
			return rows
		except:
			return []

# this function finds the highest existing customer id and adds 1 to generate a new cust id
def generateCID():
	highest_id = sql(
	'''
		SELECT c_id FROM customers
		ORDER BY c_id DESC
		LIMIT 1
	''')

	try:
		return highest_id[0][0] + 1
	except:
		return 1

def generateCartID():
	highest_id = sql(
	'''
		SELECT cart_id FROM cart
		ORDER BY cart_id DESC
		LIMIT 1
	''')

	try:
		return highest_id[0][0] + 1
	except:
		return 1

def generatePID():
	highest_id = sql(
	'''
		SELECT p_id FROM products
		ORDER BY p_id DESC
		LIMIT 1
	''')

	try:
		return highest_id[0][0] + 1
	except:
		return 1

def generateOID():
	highest_id = sql(
	'''
		SELECT o_id FROM orders
		ORDER BY o_id DESC
		LIMIT 1
	''')

	try:
		return highest_id[0][0] + 1
	except:
		return 1

# this function will add the customer into the customers table
# once they register an account
def addCustomer(request):
	sql(
		f'''
		INSERT INTO customers(c_id, c_address, c_name, c_email, c_money_spent)
		VALUES('{generateCID()}', '{request.POST["address"]}', '{request.POST["username"]}', '{request.POST["email"]}', '0')
		'''
	)
