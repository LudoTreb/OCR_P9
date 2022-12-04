"""
The form for the review.
"""


from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    """
    The review's form. With the fields headline, rating, body.
    """

    review_update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        """
        The review's model. With the fields headline, rating, body.
        """

        model = Review
        fields = ["headline", "rating", "body"]


class DeleteReviewForm(forms.Form):
    """
    The review's delete form.
    """

    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
