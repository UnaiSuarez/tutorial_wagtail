from turtle import title
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class Noticia(models.Model):
    title = models.CharField('título', max_length=250)
    resumen = models.CharField('resumen', max_length=50)
    descripcion = models.TextField('descripcion',max_length=1000, default='SOME STRING')
    imagen = models.URLField(max_length=250)

    panels = [
        FieldPanel('title'),
        FieldPanel('resumen'),
        FieldPanel('descripcion'),
        FieldPanel('imagen'),

    ]
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, videojuegos, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(videojuegos, 2)
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
        noticias = Noticia.objects.all()
        context['noticias'] = self.paginate(request, noticias)
        
        return context



class NoticiaIndexPage(Page):
    
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
            noticias = Noticia.objects.filter(title=nombre)
            qs = f'nombre={nombre}'
        else:
            noticias = None

        context['noticias'] =  noticias
        context['qs'] = qs
        
        return context
