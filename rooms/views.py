from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def see_all_rooms(request) :
    rooms = Room.objects.all() 
    # return render(request, "rooms.html")
    # 데이터 담아 보내기 
    return render(request, "rooms.html", {
        "rooms" : rooms,
        "title" : "Hello! this title comes from django!"
        }) 

def see_one_rooms(request, room_pk) :
    try :
        room = Room.objects.get(pk=room_pk)
        return render(request, "room_detail.html", {"room" : room})
    except Room.DoesNotExist : 
        # return render(request, "404.html")
        return render(request, "room_detail.html", {"not_found" : True})