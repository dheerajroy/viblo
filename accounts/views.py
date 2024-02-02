from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth.html'
    success_url = reverse_lazy('accounts:signin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Sign Up'})
        return context


class SigninView(LoginView):
    template_name = 'auth.html'
    success_url = reverse_lazy('pages:pages')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs['placeholder'] = 'username'
        form.fields['username'].label = False
        form.fields['password'].widget.attrs['placeholder'] = 'password'
        form.fields['password'].label = False

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Sign In'})
        return context
