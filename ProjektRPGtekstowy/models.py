from django.db import models

class Player(models.Model):
    curent_state=models.IntegerField(default=0)
    name=models.CharField(max_length=255)
    level=models.IntegerField(default=1)
    sil=models.IntegerField(default=1)
    szc=models.IntegerField(default=1)
    inte=models.IntegerField(default=1)
    zre=models.IntegerField(default=1)
    hp=models.IntegerField(default=15)
    hpp=models.IntegerField(default=0)
    points=models.IntegerField(default=5)

    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=6)
    description=models.TextField(null=True)
    image=models.ImageField(null=True)


    def __str__(self):
        return self.name

class Answers(models.Model):
    name=models.CharField(max_length=10)
    chance=models.FloatField(default=1)
    description=models.TextField(null=True)
    start=models.ForeignKey(Event, related_name='r_start',on_delete=models.CASCADE)
    end=models.ForeignKey(Event, related_name='r_end',on_delete=models.CASCADE)