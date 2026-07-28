from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.course, name="courses"),
    path('public_note', views.public_note, name="public_note"),
    path('notes', views.note, name="notes"),
    path('courses/add', views.add_course, name="coursesadd"),
    path('notes/add', views.add_notes, name="notesadd"),
    path('courses/edit/<slug:slug>', views.edit_course, name="editcourses"),
    path('notes/edit/<int:pk>', views.edit_note, name="editnote"),
    path('courses/delete/<slug:slug>', views.delete_course, name="deletecourses"),
    path('notes/delete/<int:pk>', views.delete_course, name="deletenotes"),
    path('courses/ditail/<slug:slug>', views.detail_course, name="ditailcourses"),
    path('notes/ditail/<int:pk>', views.detail_note, name="ditailnote"),
    path('notes/like/<int:pk>/', views.like, name='like'),
    path('bookmark',views.bookmark,name='bookmark'),
    path('bookmark/<int:pk>',views.add_bookmark,name='add_bookmark')
]
