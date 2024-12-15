from django import forms
from .models import *


class NewPostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','information','status')


