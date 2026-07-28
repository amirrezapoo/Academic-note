from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .forms import *
from .models import *
from .models import Comment, Course


# Create your views here.
def course(request):
    query = request.GET.get('q')
    courses = Course.objects.filter(author_id=request.user.id)
    if query:
        courses = courses.filter(course_name__icontains = query)
    paginator = Paginator(courses,4)
    query2 = request.GET.get('page')
    course = paginator.get_page(query2)
    return render(request, 'course/courselist.html', {'courses': course,'query':query})


def add_course(request):
    form = AddCourseForm()
    if request.method == "POST":
        form = AddCourseForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('courses')
    return render(request, 'course/addcourse.html', {'form': form})


def edit_course(request, slug):
    courses = Course.objects.get(slug=slug)
    form = EditCourseForm(instance=courses)
    if request.method == 'POST':
        form = EditCourseForm(request.POST, request.FILES, instance=courses)
        if form.is_valid():
            form.save()
            return redirect("courses")
    return render(request, 'course/editcourse.html', {'form': form})

@login_required
def delete_course(request, slug):
    courses = Course.objects.get(slug=slug)
    courses.delete()
    return redirect('courses')

@login_required
def detail_course(request, slug):
    course = Course.objects.get(slug=slug)
    note = Note.objects.filter(course = course)
    return render(request, 'course/course_detail.html', {'course': course,'note':note})

@login_required
def note(request):
    notes = Note.objects.filter(course__author_id=request.user.id, user_id=request.user.id)
    public = 0
    private =0
    for note in notes:
        if note.visibility == 'public':
            public+=1
        else:
            private +=1
    filter_type = request.GET.get('filter','all')
    sort_by = request.GET.get('sort','newest')
    if filter_type == 'private':
        notes = notes.filter(visibility = filter_type)
    elif filter_type == 'public':
        notes = notes.filter(visibility = filter_type)

    if sort_by == 'newest':
        notes = notes.order_by('-created_at')
    if sort_by == 'oldest':
        notes = notes.order_by('created_at')

    paginator = Paginator(notes,6)
    page = request.GET.get('page')
    noteobj = paginator.get_page(page)
    return render(request, 'course/notes.html', {'notes': noteobj,'sort':sort_by,'filter':filter_type,'allnote':notes,'private':private,'public':public})


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('notes')


def edit_note(request, pk):
    note = Note.objects.get(id=pk)
    form = EditNoteForm(instance=note)
    if request.method == "POST":
        form = EditNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    return render(request, 'course/edit_notes.html', {'form': form, 'note': note})


def add_notes(request):
    form = AddNoteForm(user=request.user)
    if request.method == "POST":
        form = AddNoteForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('notes')
    return render(request, 'course/add_note.html', {'form': form})


def detail_note(request, pk):

    note = Note.objects.get(id=pk)
    comments = Comment.objects.filter(note=note)
    like = Like.objects.filter(note=note, user_id=request.user.id).exists()
    views = View.objects.filter(note=note, user_id=request.user.id).exists()
    if views == False:
        View.objects.create(note=note, user_id=request.user.id)
    if note.visibility == 'private' and note.user != request.user:
        return redirect('notes')
    if like:
        is_like = True
    else:
        is_like = False
    form = CommentNoteForm()
    if request.method == 'POST':
        form = CommentNoteForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.note = note
            comment.user = request.user
            comment.save()
            comments = Comment.objects.filter(note=note)

    return render(request, 'course/note_detail.html', {'form': form, 'note': note, 'comment': comments,'is_like':is_like})


def public_note(request):
    notes = Note.public.all()
    for note in notes:
        note.is_like = Like.objects.filter(note=note,user_id=request.user.id).exists()
        note.is_bookmark = Bookmark.objects.filter(note=note,user_id=request.user.id).exists()

    query = request.GET.get('q')
    if query:
        notes = notes.filter(title__icontains = query)

    sort_by = request.GET.get('sort', 'latest')
    if sort_by == 'latest':
        notes = notes.order_by('-created_at')
    elif sort_by == 'most_liked':
        notes = notes.order_by('-likes_count')
    elif sort_by == 'most_commented':
        notes = notes.order_by('-comments_count')
    elif sort_by == 'most_viewed':
        notes = notes.order_by('-views_count')

    paginator = Paginator(notes,4)
    page = request.GET.get('page')
    objnote = paginator.get_page(page)

    return render(request, 'course/publicnotes.html', {'notes': notes,'notes2':objnote})

def like(request, pk):
    if request.method == "GET":
        note = get_object_or_404(Note, id=pk)

        like_qs = Like.objects.filter(note=note, user=request.user)

        if like_qs.exists():
            like_qs.delete()
            liked = False
        else:
            Like.objects.create(note=note, user=request.user)
            liked = True


def add_bookmark(request,pk):
    note = Note.public.get(id = pk)
    books = Bookmark.objects.filter(note = note , user=request.user).exists()
    if books == False:
        Bookmark.objects.create(note = note , user=request.user)
        return redirect('bookmark')


def bookmark(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request,'course/bookmark.html',{'bookmarks':bookmarks})