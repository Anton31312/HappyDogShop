from typing import Any
import json
from django.core.management import BaseCommand
from catalog import models

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстуры с категориями
        data_category = []
        with open('data\catalog_data.json', '+r', encoding='utf8') as file:
            json_file = json.load(file, cls=json.JSONDecoder)
            for category in json_file:
                if category['model'] == "catalog.category":
                    data_category.append(category)
            return data_category
            

        

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстуры с продуктами
        data_product = []
        with open('data\catalog_data.json', '+r', encoding='utf8') as file:
            json_file = json.load(file, cls=json.JSONDecoder)
            for product in json_file:
                if product['model'] == "catalog.product":
                    data_product.append(product)
            return data_product

    def handle(self, *args, **options):

        # Удалите все продукты
        models.Product.objects.all().delete()

		# Удалите все категории
        models.Category.objects.all().delete()

		# Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        
		# Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                models.Category(pk=category['pk'],
                                name=category['fields']['name'], 
                                description=category['fields']['description'])
            )
            

		# Создаем объекты в базе с помощью метода bulk_create()
        models.Category.objects.bulk_create(category_for_create)
        
		# Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                models.Product(pk=product['pk'],
                               name=product['fields']['name'],  
                               description=product['fields']['description'], 
						        image_product=product['fields']['image_product'],						
                                category=models.Category.objects.get(pk=product['fields']['category']), # получаем категорию из базы данных для корректной связки объектов
                                price=product['fields']['price'], 
                                created_at=product['fields']['created_at'],
                                updated_at=product['fields']['updated_at'])
            )

		# Создаем объекты в базе с помощью метода bulk_create()
        models.Product.objects.bulk_create(product_for_create)