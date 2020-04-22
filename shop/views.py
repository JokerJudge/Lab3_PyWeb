from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from .models import *

# Create your views here.


CONST = {'phone_number': PHONE_NUMBER,
        'e_mail': E_MAIL,
        'days_of_shipment': DAYS_OF_SHIPMENT,
        'site_name': SITE_NAME,
        'website': WEBSITE}

class IndexView(View):
	def get(self, request):
		return render(request, 'shop/index.html', CONST)

class ShopView(View):
    def get(self, request, page_id = 1):
        products_list = [{'name': 'Bell Pepper',
		             'image': 'shop/images/product-1.jpg',
					 'price': '$120.00',
					 'discount': '30%',
					 'price_sale': '$80.00'},
					 {'name': 'Strawberry',
		             'image': 'shop/images/product-2.jpg',
					 'price': '$120.00'},
					 {'name': 'Green Beans',
		             'image': 'shop/images/product-3.jpg',
					 'price': '$120.00'},
					 {'name': 'Purple Cabbage',
		             'image': 'shop/images/product-4.jpg',
					 'price': '$120.00'},
					 {'name': 'Tomatoe',
		             'image': 'shop/images/product-5.jpg',
					 'price': '$120.00',
					 'discount': '30%',
					 'price_sale': '$80.00'},
					 {'name': 'Brocolli',
		             'image': 'shop/images/product-6.jpg',
					 'price': '$120.00'},
					 {'name': 'Carrots',
		             'image': 'shop/images/product-7.jpg',
					 'price': '$120.00'},
					 {'name': 'Fruit Juice',
		             'image': 'shop/images/product-8.jpg',
					 'price': '$120.00'},
					 {'name': 'Onion',
		             'image': 'shop/images/product-9.jpg',
					 'price': '$120.00',
					 'discount': '30%',
					 'price_sale': '$80.00'},
					 {'name': 'Apple',
		             'image': 'shop/images/product-10.jpg',
					 'price': '$120.00'},
					 {'name': 'Garlic',
		             'image': 'shop/images/product-11.jpg',
					 'price': '$120.00'},
					 {'name': 'Chilli',
		             'image': 'shop/images/product-12.jpg',
					 'price': '$120.00'}]
		
        for product in products_list:
            p = Shop(name = product['name'], image=product['image'], price=int(product['price'][1:-3]), price_sale = 0, discount = None)
            if 'discount' in product:
                p.discount = int(product['discount'][:-1])
                p.price_sale = product['price_sale'][1:-3]
            p.save() #за один проход была сделана 1 строка в базе. p.save() - сохраняет её
		
        products = []
        for object in Shop.objects.all():
            d = dict(image=object.image, name = object.name, price = f'${object.price}', discount = f'{object.discount}%', price_sale = f'${object.price_sale}')
            products.append(d)
		
        paginator = Paginator(products, 4)
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))
        return render(request, 'shop/shop.html', {'products': products, 'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL, 'days_of_shipment': DAYS_OF_SHIPMENT, 'site_name': SITE_NAME})

class WishListView(View):
	def get(self, request):
		return render(request, 'shop/wishlist.html', CONST)

class ProductSingleView(View):
	def get(self, request):
		return render(request, 'shop/product-single.html', CONST)

class ContactView(View):
	def get(self, request):
		return render(request, 'shop/contact.html', CONST)

class CheckoutView(View):
	def get(self, request):
		return render(request, 'shop/checkout.html', CONST)

class CartView(View):
	def get(self, request):
		
		products = [{'name': 'Bell Pepper',
		             'image': 'shop/images/product-1.jpg',
					 'description': 'From sunny Argentina',
					 'price': '$4.90',
					 'quontity': '1',
					 'total': '$4.90'},
					 {'name': 'Green Peas',
					 'image': 'shop/images/product-3.jpg',
					 'description': 'Awesome Green Peas! Try!',
					 'price': '$3.80',
					 'quontity': '1',
					 'total': '$3.80'}]
		return render(request, 'shop/cart.html', {'products': products, 'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL, 'days_of_shipment': DAYS_OF_SHIPMENT, 'site_name': SITE_NAME})

class AboutView(View):
	def get(self, request):
		return render(request, 'shop/about.html', CONST)

class BlogView(View):
	def get(self, request):
		'''articles = [{'title': 'Even the all-powerful Pointing has no control about the blind texts',
		             'image': 'shop/images/image_1.jpg',
					 'q_comments': '3',
					 'date': 'July 20, 2019',
					 'author': 'Admin',
					 'description': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
					 {'title': 'Even the all-powerful Pointing has no control about the blind texts',
		             'image': 'shop/images/image_2.jpg',
					 'q_comments': '2',
					 'date': 'July 12, 2019',
					 'author': 'Gareth Emery',
					 'description': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
					 {'title': 'Even the all-powerful Pointing has no control about the blind texts',
		             'image': 'shop/images/image_3.jpg',
					 'q_comments': '0',
					 'date': 'July 08, 2019',
					 'author': 'Michael Jackson',
					 'description': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
					 {'title': 'Even the all-powerful Pointing has no control about the blind texts',
		             'image': 'shop/images/image_4.jpg',
					 'q_comments': '3',
					 'date': 'July 01, 2019',
					 'author': 'Donald Trump',
					 'description': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
					 {'title': 'Even the all-powerful Pointing has no control about the blind texts',
		             'image': 'shop/images/image_5.jpg',
					 'q_comments': '2',
					 'date': 'June 25, 2019',
					 'author': 'Admin',
					 'description': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
					 {'title': 'Even the all-powerful Pointing has no control about the blind texts',
		             'image': 'shop/images/image_6.jpg',
					 'q_comments': '3',
					 'date': 'May 28, 2019',
					 'author': 'Admin',
					 'description': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'}]
		'''
		blogs = []
		for object in Blogs.objects.all():
			d = dict(image=object.image,
				date = object.date,
				author = object.author,
				count_message = object.count_message,
				title = object.title,
				main_text = object.main_text)
			blogs.append(d)
		
		return render(request, 'shop/blog.html', {'articles': blogs, 'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL, 'days_of_shipment': DAYS_OF_SHIPMENT, 'site_name': SITE_NAME})

class BlogSingleView(View):
	def get(self, request):
		return render(request, 'shop/blog-single.html', CONST)
