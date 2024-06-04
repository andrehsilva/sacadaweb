from django.db import models
import uuid
from django.contrib.auth.models import User



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.name
    



class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Autor')
    name = models.CharField(max_length=255, verbose_name='Título')
    image = models.ImageField(
        null=True, blank=True, default="default.jpg", upload_to='images/',  verbose_name='Imagem')
    short_description = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Descrição Curta')
    description = models.TextField(null=True, blank=True,verbose_name='Descrição')
    categories = models.ManyToManyField('Category', blank=True , verbose_name='Categorias' )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    id = models.UUIDField(default = uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    class Meta:
        verbose_name = ("Postagem")
        verbose_name_plural = ("Postagens")

    def __str__(self):
        return self.name