from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Offering

def home(request):
    context = {
        'offerings': Offering.objects.all()
    }
    return render(request, 'curriculum/home.html', context)

class OfferingListView(ListView):
    model = Offering
    template_name = 'curriculum/home.html'
    context_object_name = 'offerings'

class OfferingDetailView(DetailView):
    model = Offering

class OfferingCreateView(LoginRequiredMixin, CreateView):
    model = Offering
    fields = ['code', 'name', 'web_description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfferingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Offering
    fields = ['code', 'name', 'web_description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        offering = self.get_object()
        if self.request.user == offering.created_by:
            return True
        return False

class OfferingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offering
    success_url = '/'

    def test_func(self):
        offering = self.get_object()
        if self.request.user == offering.created_by:
            return True
        return False

def about(request):
    return render(request, 'curriculum/about.html')