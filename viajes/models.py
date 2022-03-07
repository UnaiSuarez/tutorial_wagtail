from turtle import title
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class Viaje(models.Model):
    destino = models.CharField('destino', max_length=50)
    coordenadas = models.CharField('coordenadas', max_length=250)
    descripcion = models.TextField('descripcion',max_length=1000, default='SOME STRING')
    imagen = models.URLField(max_length=250)

    panels = [
        FieldPanel('destino'),
        FieldPanel('coordenadas'),
        FieldPanel('descripcion'),
        FieldPanel('imagen'),

    ]
    def __str__(self):
        return f'{self.destino}'
    
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

class ViajesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, viajes, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(viajes, 15)
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
        viajes = Viaje.objects.all()
        context['viajes'] = self.paginate(request, viajes)
        
        return context



class ViajeIndexPage(Page):
    
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        destino = request.GET.get('destino')
        qs = ''
        if destino:
            viajes = Viaje.objects.filter(destino=destino)
            qs = f'destino={destino}'
        else:
            viajes = None

        context['viajes'] =  viajes
        context['qs'] = qs
        
        return context
