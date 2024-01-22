from django.db import models
from PIL import Image
import os
from django.conf import settings


class Produto(models.Model):
    nome = models.CharField(max_length=300)
    descricao_curta = models.TextField(max_length=300)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )
        
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_name = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_name)
        original_width, original_heigth = img_pil.size
        
        if original_width <= new_width:
            img_pil.close()
            #print('a imagem NAO foi redimencionada')
            return
        
        new_heigth = round((new_width * original_heigth) / original_width)
        new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
        new_img.save(
            img_full_name,
            optimize=True,
            quality=60,
        )
        #print('a imagem foi redimencionada')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        max_image_size = 800
        
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)
                
    def __str__(self):
        return self.nome
    
    
class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=300, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nome or self.produto.nome
    
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

""" 
    Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int
"""