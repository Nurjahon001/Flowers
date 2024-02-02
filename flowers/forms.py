from django import forms
from .models import FlowerReview

class FlowerReviewForm(forms.ModelForm):
    class Meta:
        model = FlowerReview
        fields = ['star_given', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }