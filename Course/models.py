from django.db import models
from django.utils.text import slugify

from account.models import User

cho = (
    ('semester1', 'semster1'),
    ('semester2', 'semster2'),
    ('semester3', 'semster3'),
    ('semester4', 'semster4'),
    ('semester5', 'semster5'),
    ('semester6', 'semster6'),
    ('semester7', 'semster7'),
    ('semester8', 'semster8'),
)
cho2 = (
    ('1 unit', '1 unit'),
    ('2 unit', '2 unit'),
    ('3 unit', '3 unit'),
    ('4 unit', '4 unit'),
)
ch3 = (
    ('private', 'private'),
    ('public', 'public')
)
class CustomNote(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(visibility = 'public')

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    semester = models.CharField(choices=cho, max_length=100)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='image/course', default='image/course/course default.png', blank=True,
                              null=True)
    credit_units = models.CharField(choices=cho2, max_length=100)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.course_name)
        super().save(*args,**kwargs)

    def total_note(self):
        return self.notes.count()

    def total_note_public(self):
        return self.notes.filter(visinility='public').count()
    def __str__(self):
        return self.course_name


class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/note', null=True, blank=True)
    file = models.FileField(upload_to='file/note', null=True, blank=True)
    tags = models.CharField(max_length=500)
    context = models.TextField()
    visibility = models.CharField(max_length=200,choices=ch3)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    public = CustomNote()

    def __str__(self):
        return self.title

    def total_likes(self):

        return self.likes.count()

    def total_bookmarks(self):

        return self.bookmarks.count()

    def total_views(self):

        return self.views.count()

    def total_comments(self):

        return self.comments.count()


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    note = models.ForeignKey(Note,on_delete=models.CASCADE,related_name='likes')

    def __str__(self):
        return self.user.username

class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='views')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='views')

    def __str__(self):
        return self.user.username


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user','note')


    def __str__(self):
        return self.user.username


class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    context = models.TextField()
    replied = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)


