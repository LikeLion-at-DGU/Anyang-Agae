from django import forms
from django.contrib.auth.models import User
from users.models import Profile

OPENED_CHOICES = [
    ('OPEN', '공개'),
    ('NOT_OPEN', '비공개'),
]


class SignupForm(forms.Form):
    class Meta:
        model = User

    is_opened = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPENED_CHOICES
    )

    def signup(self, request, user):
        userProfile = Profile()
        userProfile.user = user
        userProfile.is_opened = self.cleaned_data['is_opened']
        userProfile.save()
        user.save()
        return user
