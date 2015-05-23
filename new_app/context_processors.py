
from models import *


TRACKS = None

def base(request):
    global TRACKS
    if not TRACKS:
        TRACKS = Track.objects.all()


    return {'tracks': TRACKS ,}



