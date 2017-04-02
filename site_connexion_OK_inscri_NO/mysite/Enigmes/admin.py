from django.contrib import admin

# Register your models here.
from .models import Enigmes
from .models import Joueur



class EnigmesAdmin(admin.ModelAdmin):

   list_display   = ('numero', 'question', 'reponse')

   list_filter    = ('question','auteur',)

   #date_hierarchy = ('numero')

   ordering       = ('numero', )

   search_fields  = ('question', 'numero')

admin.site.register(Enigmes,EnigmesAdmin)
admin.site.register(Joueur)