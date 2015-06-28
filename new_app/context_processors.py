
from models import *


TRACKS = None

def base(request):
    context = {}

    global TRACKS
    # if not TRACKS:
    TRACKS = Track.objects.all()
    context['tracks'] = TRACKS


    notifications = None
    if request.user.is_authenticated():
        all_n = request.user.notifications.unread()
        final_n = {}
        for n in all_n:
            if n.target.id in final_n.keys():
                final_n[n.target.id].others += 1
            else:
                n.others = 0
                final_n[n.target.id] = n
        context['notifications'] = final_n.values()

    return context




