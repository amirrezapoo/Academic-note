from django import forms
from .models import Course, Note,Comment


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug', 'author')
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Advanced Programming", 'type': 'text'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'credit_units': forms.Select(attrs={'class': 'form-select'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Write a short description about this course..."}),
            'image': forms.FileInput(attrs={'type': "file", 'class': "form-control mt-3"}),
            'is_active': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': "checkbox"})
        }


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug', 'author')
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Advanced Programming", 'type': 'text'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'credit_units': forms.Select(attrs={'class': 'form-select'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Write a short description about this course..."}),
            'image': forms.FileInput(attrs={'type': "file", 'class': "form-control mt-3"}),
            'is_active': forms.CheckboxInput(attrs={'class': "form-check-input", 'type': "checkbox"})
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('image','title','context','visibility','tags','file')
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'tags':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'visibility':forms.Select(attrs={'class':'form-select'}),
            'context':forms.Textarea(attrs={'class':'form-control','type':'text'}),
            'file': forms.FileInput(attrs={'type': "file", 'class': "form-control"}),
            'image': forms.FileInput(attrs={'type': "file", 'class': "form-control"}),
        }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('image', 'title', 'context', 'visibility', 'tags', 'file', 'course')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'visibility': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'type': 'text'}),
            'file': forms.FileInput(attrs={'type': "file", 'class': "form-control", 'accept': '.pdf.doc.txt'}),
            'image': forms.FileInput(attrs={'type': "file", 'class': "form-control", 'accept': 'image/*'}),
        }

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user',None)
        super().__init__(*args,**kwargs)

        if user:
            self.fields['course'].queryset = user.courses.all()
            if not user.courses.exists():
                self.fields['course'].empty_label = 'No course found . create the course first'


class CommentNoteForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ('context',)
        widgets = {
            'context':forms.Textarea(attrs={'class':'form-control'})
        }