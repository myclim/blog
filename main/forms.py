from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Posts
from django.contrib.auth import get_user_model


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title", "text")


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title", "text")


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password",
        )
