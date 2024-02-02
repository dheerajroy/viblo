from django.urls import path
from .views import CreatePageView, ListPagesView, PageView, UpdatePageView, DeletePageView

app_name = 'pages'

urlpatterns = [
    path('create', CreatePageView.as_view(), name='create'),
    path('', ListPagesView.as_view(), name='pages'),
    path('<slug:slug>', PageView.as_view(), name='page'),
    path('<slug:slug>/update', UpdatePageView.as_view(), name='update'),
    path('<slug:slug>/delete', DeletePageView.as_view(), name='delete'),
]
