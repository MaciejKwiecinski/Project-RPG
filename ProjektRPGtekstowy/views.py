from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .models import Player,Event,Answers
from .forms import PlayerForm,AnswersForm,Player2Form

# Create your views here.

def main(request):
    return render(request, 'index.html')

class Base(View):
    def get(self,request):
        play=Player.objects.latest('id')
        form=PlayerForm(instance=play)
        return render(request,'base.html',{'stats':form})



class PlayerView(View):
    def get(self,request):
        form=PlayerForm()
        return render(request,'create.html',{'form':form})

    def post(self,request):
        form=PlayerForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            sil=form.cleaned_data['sil']
            szc=form.cleaned_data['szc']
            inte=form.cleaned_data['inte']
            zre=form.cleaned_data['zre']
            hp=form.cleaned_data['hp']
            points=form.cleaned_data['points']
            Player.objects.create(name=name,sil=sil,szc=szc,inte=inte,zre=zre,hp=hp,points=points)
            return redirect('/story/3')
        return render(request,'create.html',{'form':form})

class EventView(View):
    def get(self,request,id):
        miejsce=Event.objects.get(id=id)
        answers=Answers.objects.filter(start_id=id)
        player=Player.objects.latest('id')
        player.curent_state=id
        return render(request,'history.html',{'event':miejsce,'answers':answers})

    def post(self,request,id):
        end_id=request.POST['end']
        return redirect(f'/story/{end_id}')

class StatView(View):
    def post(self,request):
        player=Player.objects.latest('id')
        form=Player2Form(request.POST,instance=player)
        if form.is_valid():
            form.save()
        adr = request.META.get('HTTP_REFERER')
        return redirect(adr)

class CharacterView(View):
    def get(self,request):
        player=Player.objects.latest('id')
        return render(request,'character.html',{'player':player})

def instruction(request):
    return render(request,'instruction.html')






