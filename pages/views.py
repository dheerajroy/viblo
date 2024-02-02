from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import Http404
from .models import Page
from .forms import CreateUpdatePageForm


class CreatePageView(LoginRequiredMixin, CreateView):
    form_class = CreateUpdatePageForm
    template_name = 'create_update_page.html'

    def get_success_url(self):
        return reverse('pages:page', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Create'})
        return context


class ListPagesView(LoginRequiredMixin, ListView):
    template_name = 'pages.html'
    context_object_name = 'pages'
    paginate_by = 20

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user).order_by('-id')


class PageView(DetailView):
    template_name = 'page.html'
    model = Page
    context_object_name = 'page'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if data['page'].author == self.request.user or not data['page'].private:
            return data
        raise Http404()


class UpdatePageView(LoginRequiredMixin, UpdateView):
    form_class = CreateUpdatePageForm
    template_name = 'create_update_page.html'
    slug_field = 'slug'

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('pages:page', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Update'})
        return context


class DeletePageView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_page.html'
    context_object_name = 'page'
    slug_field = 'slug'
    success_url = reverse_lazy('pages:pages')

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)
