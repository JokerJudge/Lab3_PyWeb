from django.db import models

# Create your models here.

'''class Fruit(model.Model):
	name = 
	image = 
	price = 
	discount = 
	price_sale = '''


class Blogs(models.Model):
	id = models.AutoField(primary_key = True)
	image = models.CharField(max_length=64)
	date = models.DateTimeField(auto_now = True)
	author = models.CharField(max_length=32, default = 'Admin')
	count_message = models.PositiveIntegerField(default = 0)
	title = models.CharField(max_length=100, null = False)
	main_text = models.CharField(max_length=500,null = False)
	
	def __str__(self):
		 return f'{self.id} - {self.title}'

class Shop(models.Model):
	price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField(null = True)
	price_sale = models.PositiveIntegerField()
	image = models.CharField(max_length=64)
	name = models.CharField(max_length=64, primary_key = True)
	
	def __str__(self):
		 return f'{self.name}'