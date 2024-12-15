# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import Post  # Ensure the Post model is correctly imported

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'information', 'email', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('title'),
            FloatingField('information'),
            FloatingField('email'),
            FloatingField('status'),
            Submit('submit', 'Submit')
        )
