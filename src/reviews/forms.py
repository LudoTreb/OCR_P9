from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    review_update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
