from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from videojuegos.models import Consola, Genre, Videojuego


'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''


class GenerosAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Genre
    menu_label = 'Géneros'
    search_fields = ('nombre',)
    menu_icon = 'fa-tags'
    
class ConsolasAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Consola
    menu_label = 'Consolas'
    search_fields = ('nombre',)
    menu_icon = 'fa-tags'


class Juegosdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Videojuego
    search_fields = ('title',)
    menu_icon = 'fa-film'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)



class VideojuegosAdminGroup(ModelAdminGroup):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    menu_label = 'Videojuegos'
    menu_icon = 'fa-film'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (GenerosAdmin, ConsolasAdmin ,Juegosdmin, )


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(VideojuegosAdminGroup)
