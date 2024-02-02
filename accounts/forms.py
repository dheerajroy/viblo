from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = False

        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = False

        self.fields['password2'].widget.attrs['placeholder'] = 'confirm your password'
        self.fields['password2'].label = False
        self.fields['password2'].help_text = False
