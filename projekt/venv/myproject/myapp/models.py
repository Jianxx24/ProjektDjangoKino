from django.db import models
from django.contrib.auth.models import User
import locale
locale.setlocale(locale.LC_TIME, "pl_PL")



class Movie(models.Model):
    title=models.CharField(max_length=100)
    duration=models.IntegerField()
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    image=models.ImageField(null=True, upload_to='./')

class Seat(models.Model):
    pos_x=models.IntegerField()
    pos_y=models.IntegerField()

class Show(models.Model):
    movie=models.ForeignKey('Movie', on_delete=models.CASCADE)
    date=models.DateTimeField()
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(Show, self).save(*args, **kwargs)
        if is_new:
            
            cd = Seat.objects.all()
            for seat in cd:
                Ticket.objects.create(show=self,seat=seat)

class Ticket(models.Model):
    show=models.ForeignKey('Show', on_delete=models.CASCADE)
    seat=models.ForeignKey('Seat', on_delete=models.CASCADE)
    person=models.BooleanField(default=False)

class Order(models.Model):
    ticket=models.ForeignKey('Ticket',on_delete=models.SET_NULL, null=True)
    date_ordered=models.DateTimeField(auto_now=True)
    person=models.ForeignKey(User, on_delete=models.CASCADE)

class OrderList(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)



# Create your models here.

