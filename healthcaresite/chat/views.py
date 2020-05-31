from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# Create your views here.
# def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    # room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    # messages = reversed(room.messages.order_by('-timestamp')[:50])

    # return render(request, "chat/room.html", {
    #     'room': room,
    #     'messages': messages,
    # })

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })