from django import forms
from . import models

class ShowForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'
