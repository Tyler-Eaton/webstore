from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.functions import sql, generateCartID, generateOID
from datetime import timedelta, date
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
	try:
		get_cid = sql(f'''
				SELECT c_id
				FROM customers
				WHERE c_name = '{request.user}'
				''')[0][0]

		cart = sql(f'''
			SELECT *
			FROM cart c, customers cu, products p
			WHERE cu.c_id = c.c_id AND p.p_id = c.p_id AND c.c_id = {get_cid}
			''')
		return render(request, "cart/index.html", {"cart":cart})
	except:
		print("out of range")
		return render(request, "cart/index.html", {"cart":[]})

@login_required
def removecart(request):
	if request.method == 'POST':
		try:
			get_cid = sql(f'''
				SELECT c_id
				FROM customers
				WHERE c_name = '{request.user}'
				''')[0][0]
			sql(f'''
				DELETE FROM cart
				WHERE c_id = {get_cid} and p_id = {request.POST['id']}
				'''
			)
			return redirect("/cart/")
		except:
			print("Cannot delete from cart")
			return redirect('/')

@login_required
def addcart(request):
	if request.method == 'POST':
		try:
			get_cid = sql(f'''
				SELECT c_id
				FROM customers
				WHERE c_name = '{request.user}'
				''')[0][0]
			find_existing = sql(f'''
					SELECT *
					FROM cart
					WHERE c_id = {get_cid} AND p_id = {request.POST['id']}
							''')
			if not find_existing:
				sql(f'''
						INSERT INTO cart (cart_id,p_id,c_id) values({generateCartID()}, {request.POST['id']}, {get_cid})
						'''
					)
				messages.success(request, "Item added to cart")
				return redirect("/cart/")
			else:
				messages.error(request, "Item is already in your cart")
				return redirect("/cart/")
		except:
			print("Cannot Add to cart")
			return redirect('/')

@login_required
def checkout(request):
	try:
		order_date = str(date.today())
		ship_date = str(date.today() + timedelta(days=1))
		deliver_date = str(date.today() + timedelta(days=2))

		get_cid = sql(f'''
			SELECT c_id
			FROM customers
			WHERE c_name = '{request.user}'
			''')[0][0]

		get_cart = sql(f'''
				select * from cart
				WHERE c_id = {get_cid}
					''')
		total_price = 0
		# update quantity
		for row in get_cart:
			p_id = row[1]

			initial_qty = sql(f'''
				SELECT p_quantity from PRODUCTS
				WHERE p_id = {p_id}
					''')[0][0]
			initial_qty -= 1
			price = sql(f'''
				SELECT p_price from PRODUCTS
				WHERE p_id = {p_id}
					''')[0][0]
			total_price += price
			sql(f'''
				UPDATE products
				SET p_quantity = {initial_qty}
				WHERE p_id = {p_id}
					''')

			# insert order into orders table
			sql(f'''
				INSERT INTO orders (o_num_items, c_id, p_id, o_shipdate, o_deliverdate, o_orderdate, o_id)
				VALUES ({len(get_cart)}, {get_cid}, {p_id}, '{ship_date}', '{deliver_date}', '{order_date}', {generateOID()})
				''')

			# remove from cart
			sql(f'''
				DELETE FROM cart
				WHERE c_id = {get_cid} and p_id = {p_id}
				''')

		# update total money spent for the customer
		inital_money_spent = sql(f'''
		SELECT c_money_spent FROM customers
		WHERE c_id = {get_cid}
		''')[0][0]
		total_price += inital_money_spent
		sql(f'''
			UPDATE customers
			SET c_money_spent = {total_price}
			WHERE c_id = {get_cid}
			'''
		)

		address = sql(f'''
					SELECT c_address FROM customers
					WHERE c_id = {get_cid}
					''')[0][0]

		return render(request, "cart/checkout.html", {"deliver_date":deliver_date, "user_address":address})

	except:
		print("An error has occured")
		return redirect("/cart/")