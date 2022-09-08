from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':"Let's learn python!"},
#     {'id':2, 'name':"Design with us"},
#     {'id':3, 'name':"Frontend developers"},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    #get is for a unique identifying value
    room = Room.objects.get(id=pk)
    context = {'room': room}
    
    return render(request, 'base/room.html', context)