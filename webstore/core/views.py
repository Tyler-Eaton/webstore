from django.shortcuts import render, redirect
from .forms import SignupForm
from .functions import sql, addCustomer, generateCartID
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# Create your views here.
def base(request):
	return render(request, 'core/base.html')

def index(request):
	rows = sql("SELECT * FROM products ORDER BY RANDOM() LIMIT 3")
	return render(request, 'core/index.html', {"rows":rows})

def about(request):
	return render(request, "core/about.html")

def contact(request):
	return render(request, "core/contact.html")

def products(request):
	if request.method == "POST":
		rows = sql(f"SELECT * FROM products WHERE lower(p_brand) = '{request.POST['brand'].lower()}'")
	else:
		rows = sql("SELECT * FROM products")

	return render(request, 'core/products.html', {"rows":rows, "results":len(rows)})

def orders(request):
	# get order info
	get_cid = sql(f'''
				SELECT c_id
				FROM customers
				WHERE c_name = '{request.user}'
				''')[0][0]
	orders = sql(f'''
		SELECT o.o_deliverdate, o.o_orderdate, o.o_shipdate, o.p_id, p.p_name,
				p.p_brand, p.p_description, p.p_imgurl, p.p_price
		FROM orders o, products p
		WHERE c_id = {get_cid} AND p.p_id = o.p_id
		GROUP BY o.o_shipdate, o.c_id, o.p_id, o.o_deliverdate, o.o_orderdate, o.o_shipdate,
				p.p_name, p.p_brand, p.p_description, p.p_imgurl, p.p_price
				''')
	return render(request, 'core/orders.html', {"orders":orders})

def logout_view(request):
	logout(request)
	return redirect("/login/")

def productCart(request):
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

def register(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()
			addCustomer(request)
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			return redirect("/")
	else:
		form = SignupForm()

	return render(request, 'core/register.html', {'form':form})

