from account.models import User
from Course.models import *


def notes(request):
    notes = Note.objects.filter(user_id=request.user.id).count()
    return {'notes':notes}

def course(request):
    course = Course.objects.filter(author_id=request.user.id).count()
    return {'course':course}

def public_notes(request):
    public = Note.public.filter(user_id=request.user.id).count()
    return {'public':public}

def bookmark(request):
    books = Bookmark.objects.filter(user_id=request.user.id).count()
    return {'bookmark':books}

def recent_notes(request):
    notes = Note.objects.filter(user_id=request.user.id).order_by('-created_at')[:3]
    return {'recentnote':notes}

def recent_public(request):
    notes = Note.public.all().order_by('-created_at')[:3]
    return {'recentpublic':notes}