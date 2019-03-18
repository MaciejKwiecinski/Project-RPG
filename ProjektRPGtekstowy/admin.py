from django.contrib import admin
from .models import Player,Answers,Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
admin.site.register(Event, EventAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','start','end')
admin.site.register(Answers, AnswerAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','user_players','level','name','curent_state','sil','szc','inte','zre','hp','hpp','points')
admin.site.register(Player, PlayerAdmin)




