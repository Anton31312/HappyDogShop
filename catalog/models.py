from django.db import models

NULLABLE = {'blank': True, 'null':True}

class Category(models.Model):
    
    name = models.CharField(max_length=130, verbose_name='Название категории')
    description = models.CharField(max_length=550, verbose_name='Описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)

class Product(models.Model):
    
    name = models.CharField(max_length=130, verbose_name='Название')
    description = models.CharField(max_length=550, verbose_name='Описание', **NULLABLE)
    image_product = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField(default=1, verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')
    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULLABLE)
    
    def __str__(self):
        return f'{self.name} {self.description}'
    
    class Meta():
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)