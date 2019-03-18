from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Player,Event,Answers
from .forms import PlayerForm,Player2Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from random import choice


@login_required
def main(request):
    request.session['player_id']=request.user.id
    return render(request, 'index.html')

class Base(LoginRequiredMixin,View):
    def get(self,request):
        play=Player.objects.get(id=request.user.id)
        form=PlayerForm(instance=play)
        return render(request,'base.html',{'stats':form})

class PlayerView(LoginRequiredMixin,View):
    def get(self,request):
        form=PlayerForm()
        return render(request,'create.html',{'form':form})

    def post(self,request):
        form=PlayerForm(request.POST)
        usr=request.user
        user=User.objects.get(id=usr.id)
        if form.is_valid():
            name=form.cleaned_data['name']
            sil=form.cleaned_data['sil']
            szc=form.cleaned_data['szc']
            inte=form.cleaned_data['inte']
            zre=form.cleaned_data['zre']
            hp=form.cleaned_data['hp']
            point=(sil-1)+(szc-1)+(inte-1)+(zre-1)+((hp-15)/5)
            points=5-point
            player=Player.objects.create(user_players=user,name=name,sil=sil,szc=szc,inte=inte,zre=zre,hp=hp,points=points)
            request.session['character_id']=player.id
            return redirect(f'/character/{player.id}')
        return render(request,'create.html',{'form':form})

class CharactersView(LoginRequiredMixin,View):
    def get(self,request):
        players = Player.objects.filter(user_players_id=request.session.get('player_id'))
        return render(request,'characters.html',{'characters':players})

    def post(self,request):
        id=request.POST['idik']
        request.session['character_id']=id
        return redirect(f'character/{id}')

class EventView(LoginRequiredMixin,View):
    def get(self,request,id):
        random=0
        miejsce=Event.objects.get(id=id)
        answers=Answers.objects.filter(start_id=id)
        player=Player.objects.get(user_players_id=request.session.get('player_id'),id=request.session.get('character_id'))
        player.curent_state=id
        player.hpp=player.hpp+1
        if miejsce.is_random == True:
            random=choice(answers)
            random=random.end_id
        if player.hpp>8:
            player.level=player.level+1
            player.points=player.points+5
            player.hpp=player.hpp-8
        player.save()
        if miejsce.id == 58:
            player.delete()
        return render(request,'history.html',{'event':miejsce,'answers':answers,'random':random})

    def post(self,request,id):
        end_id=request.POST['end']
        return redirect(f'/story/{end_id}')

class StatView(LoginRequiredMixin,View):
    def post(self,request):
            id=request.session['character_id']
            player=Player.objects.get(id=id)
            form=Player2Form(request.POST,instance=player)
            if form.is_valid():
                form.save()
            else:
                request.session['Errors']='za dużo dodanych punktów'
            adr = request.META.get('HTTP_REFERER')
            return redirect(adr)

class CharacterView(LoginRequiredMixin,View):
    def get(self,request,id):
        if Player.objects.exists():
            player = Player.objects.get(user_players_id=request.session.get('player_id'), id=request.session.get('character_id'))
            return render(request,'character.html',{'player':player})
        else:
            return render(request,'index.html')
@login_required
def instruction(request):
    return render(request,'instruction.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})