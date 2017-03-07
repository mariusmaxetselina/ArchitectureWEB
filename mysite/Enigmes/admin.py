from django.contrib import admin

# Register your models here.
from .models import Enigmes




class EnigmesAdmin(admin.ModelAdmin):

   list_display   = ('numero', 'question', 'reponse')

   list_filter    = ('question','auteur',)

   #date_hierarchy = ('numero')

   ordering       = ('numero', )

   search_fields  = ('question', 'numero')

admin.site.register(Enigmes,EnigmesAdmin)