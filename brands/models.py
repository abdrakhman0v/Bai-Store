from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название бренда")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    #logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"