from .models import Player
from .forms import Player2Form

def my_cp(request):
    play = Player.objects.latest('id')
    form = Player2Form(instance=play)
    ctx = {"stats":form}
    return ctx