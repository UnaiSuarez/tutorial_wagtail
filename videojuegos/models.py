import re
from turtle import title
from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify

# Create your models here.
class Genre(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.nombre
    panels = [
        FieldPanel('nombre')
    ]
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        
class Consola(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.nombre
    panels = [
        FieldPanel('nombre')
    ]
    class Meta:
        verbose_name = 'Consola'
        verbose_name_plural = 'Consolas'
                
        
class Videojuego(models.Model):
    title = models.CharField('título', max_length=250)
    descripcion = models.TextField('descripcion',max_length=1000, default='SOME STRING')
    precio = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    rating = models.DecimalField(max_digits=6, decimal_places=0,default=0)
    link = models.URLField()
    imagen = models.URLField(max_length=250)
    generos = models.ManyToManyField(Genre)
    consolas = models.ManyToManyField(Consola)

    panels = [
        FieldPanel('title'),
        FieldPanel('descripcion'),
        FieldPanel('rating'),
        FieldPanel('precio'),
        FieldPanel('link'),
        FieldPanel('imagen'),
        FieldPanel('generos'),
        FieldPanel('consolas')

    ]
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'

class VideojuegosIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, videojuegos, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(videojuegos, 15)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        plataforma = request.GET.get('plataforma')
        genero = request.GET.get('genero')
        qs = ''
        if plataforma:
            videojuegos = Videojuego.objects.filter(consolas__nombre=plataforma).order_by('-rating')
            qs = f'plataforma={plataforma}'
        elif genero:
            videojuegos = Videojuego.objects.filter(generos__nombre=genero).order_by('-rating')
            qs = f'plataforma={plataforma}'
        else:
            videojuegos = Videojuego.objects.all().order_by('-rating')

        context['videojuegos'] = self.paginate(request, videojuegos)
        context['qs'] = qs
        context['consolas'] = Consola.objects.all()
        context['generos'] = Genre.objects.all()
        
        return context



class VideojuegoIndexPage(Page):
    
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        nombre = request.GET.get('nombre')
        qs = ''
        if nombre:
            videojuegos = Videojuego.objects.filter(title=nombre)
            qs = f'plataforma={nombre}'
        else:
            videojuegos = None

        context['videojuegos'] =  videojuegos
        context['qs'] = qs
        context['consolas'] = Consola.objects.all()
        context['generos'] = Genre.objects.all()
        
        return context



    