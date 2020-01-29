from django.contrib import admin
from .models import *
from django.contrib.admin import site

admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Show)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(OrderList)
# Register your models here.
