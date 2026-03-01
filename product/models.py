from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Базовая цена")
    price_cash = models.PositiveIntegerField(verbose_name="Цена наличными", null=True, blank=True)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    brand = models.ForeignKey('brands.Brand', on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="Бренд")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Главное фото")

    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    is_hit = models.BooleanField(default=False, verbose_name="Хит продаж")
    is_new = models.BooleanField(default=False, verbose_name="Новинка")
    
    # Характеристики (для процессора, памяти и т.д. из Figma)
    specifications = models.JSONField(default=dict, blank=True, verbose_name="Характеристики (JSON)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.title