from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','credit_units','semester')
    list_filter = ('semester',)
    search_fields = ('course_name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','user','course','visibility')
    list_editable = ('visibility',)
    list_filter = ('visibility','course','user')

@admin.register(Bookmark)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('note','user',)
    list_filter = ('note','user')

@admin.register(Comment)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('note','user',)
    list_filter = ('note','user')

admin.site.register(Like)
admin.site.register(View)