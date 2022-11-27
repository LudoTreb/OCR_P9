from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # TODO: usually better to specify each field instead of using all
        fields = '__all__'
