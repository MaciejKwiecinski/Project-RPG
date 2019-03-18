from .models import Player
from .forms import Player2Form

def my_cp(request):
    try:
        play = Player.objects.get(user_players_id=request.session.get('player_id'),id=request.session.get('character_id'))
        form = Player2Form(instance=play)
        ctx = {"stats":form}
    except:
        ctx={'stats':'Brak gracza'}
    return ctx