from django.contrib import admin
from .models import Player,Answers,Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
admin.site.register(Event, EventAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','start','end')
admin.site.register(Answers, AnswersAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','name','curent_state','sil','szc','inte','zre','hp','hpp')
admin.site.register(Player, PlayerAdmin)




