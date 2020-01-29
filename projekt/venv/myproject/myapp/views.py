from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib import messages


def delete(request, id):
    if (request.user.is_authenticated):
        if(request=='POST'):
            form=OrderDeleteForm(request.POST)
    else:
        return render(request, 'login.html')


def orderHandling(request):
    if(request.user.is_authenticated):
        orders=OrderList.objects.filter(person=request.user).order_by('ticket__show__date','ticket__show__movie__title','ticket__seat__pos_x')
        if(request.method=="POST"):
            if 'delete' in request.POST:
                OrderList.objects.filter(id=request.POST.get('delete')).delete()
                return redirect(orderHandling)
            else:
                for o in orders:
                    o.ticket.person=True
                    o.ticket.save()
                    Order.objects.create(person=o.person, ticket=o.ticket)
                    OrderList.objects.filter(person=request.user).delete()
                return redirect('mytickets')
        return render(request, 'orders.html', {'orderse': orders})
    else:
        return render(request, 'login.html')



def index(request):
    movies=Movie.objects.all()
    return render(request, 'base.html',{'movies': movies})


def allshows(request):
    shows = Show.objects.all().order_by('date')
    return render(request, 'shows2.html', {'shows': shows})


def shows(request, title):
    movie=Movie.objects.get(id=title)
    shows=Show.objects.filter(movie__id=title).order_by('date')
    return render(request, 'shows.html',{'shows':shows,'movie':movie})

def loginApp(request):
    if (request.method=="POST"):
        form=LoginForm(request.POST)
        if (form.is_valid()):
            username=request.POST["login"]
            password = request.POST["password"]
            user=authenticate(request, username=username, password=password)
            if (user is not None):
                login(request, user)
                messages.success(request, 'Zalogowano pomyslnie!')
            else:
                messages.warning(request, 'Wprowadzono bledne dane!')
    if(request.user.is_authenticated):
        return render(request, 'login.html')
    else:
        form=LoginForm()
        return render(request, 'login.html', {'form': form})

def movies(request):
    movies=Movie.objects.all()
    return render(request, 'movies.html',{'movies': movies})

def tickets(request, title, tickets):
    if(request.user.is_authenticated):
        cols = Ticket.objects.all().values_list('seat__pos_y', flat=True).distinct()
        rows=[]
        t=(OrderList.objects.filter(person=request.user).values_list('ticket__id', flat=True))
        for c in cols:
            rows.append(Ticket.objects.filter(seat__pos_y=c,show__id=tickets).order_by('seat__pos_x'))
        orders=Order.objects.all()
        if(request.method=="POST"):
            form=TicketForm(request.POST)
            form.fields['tickets'].choices=[(x,x) for x in Ticket.objects.filter(show__id=tickets).values_list('seat__pos_x',flat=True)]
            if form.is_valid():
                cd=request.POST.getlist('tickets')
                OrderList.objects.bulk_create([(OrderList(person=request.user, ticket=Ticket.objects.get(seat__pos_x=i, show__id=tickets))) for i in cd])
                return redirect('orders')
        return render(request, 'tickets.html', {'rows':rows, 't':t})
    else:
        return render(request, 'login.html')


def movie(request, title):
    movie=Movie.objects.get(pk=title)
    print(movie)
    show=Show.objects.filter(movie=movie)
    return render(request,'movie.html', {'movie':movie,'show':show})

    
    
def register(request):
    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=request.POST["login"]
            email=request.POST["email"]
            password=request.POST["password"]
            user, created=User.objects.get_or_create(username=username, email=email)
            if(created):
                user.set_password(password)
                user.save()
                return redirect('/cinema/login/')
            else:
                messages.warning(request, 'Uzytkownik jest w bazie')
    if(not request.user.is_authenticated):
        form=RegisterForm()
        return render(request, 'register.html', {'form':form})
    else:
        return redirect('/cinema/login/')

def mytickets(request):
    if(request.user.is_authenticated):
        orderse=Order.objects.filter(person=request.user).order_by('date_ordered')
        return render(request,'mytickets.html' , {'orderse' : orderse})
    else:
        return render(request, 'login.html')



