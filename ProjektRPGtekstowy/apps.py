from django.apps import AppConfig
from django.contrib import admin
from .models import Player,Answers,Event

class ProjektrpgtekstowyConfig(AppConfig):
    name = 'ProjektRPGtekstowy'

class EventAdmin(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(Event, EventAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('name','description','start','end')
admin.site.register(Answers, AnswersAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','curent_state','sil','szc','int','zre','hp','hpp','points')
admin.site.register(Player, PlayerAdmin)



