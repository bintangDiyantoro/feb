from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from .validators import validateWriter
# Create your models here.

lorem = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita, animi! Accusantium quis sunt vitae, iste sit voluptate eos saepe adipisci cupiditate ratione harum qui vel at reiciendis maiores? Illum fugiat consequuntur quibusdam architecto ullam, optio qui quas ut nesciunt obcaecati maiores beatae minus error praesentium corporis fuga distinctio, quisquam excepturi.'

class Artikel(models.Model):
    judul = models.CharField(max_length=50, unique=True)
    isi = models.TextField(max_length=1000, default=lorem)
    penulis = models.CharField(max_length=30, validators=[validateWriter])
    foto = models.FileField()
    slug = models.SlugField(blank=True, editable=False)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self):
        self.slug = slugify(self.judul)
        return super(Artikel, self).save()
    
    def get_absolute_url(self):
        return reverse('blog:index')

    def __str__(self):
        return self.judul
