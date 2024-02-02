from django import forms
from .models import Page
from ckeditor.widgets import CKEditorWidget


class CreateUpdatePageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'private', 'content']
        widgets = {
            'content': CKEditorWidget()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'title'
        self.fields['title'].label = False
        self.fields['content'].widget.attrs['placeholder'] = 'content'
        self.fields['content'].label = False
