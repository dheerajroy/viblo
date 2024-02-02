from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignupView, SigninView

app_name = 'accounts'

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('signin', SigninView.as_view(), name='signin'),
    path('signout', LogoutView.as_view(), name='signout'),
]
