from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import PropertyModel
from django.urls import reverse_lazy
from django.db.models import Q

class PropertyList(ListView):
    template_name = 'home.html'
    model = PropertyModel
    ordering = ['-postdate']
    paginate_by = 5

class PropertyDetail(DetailView):
    template_name = 'detail.html'
    model = PropertyModel

class PropertyCreate(CreateView):
    template_name = 'create.html'
    model = PropertyModel
    fields = ('property_name', 'school_name', 'content', 'evaluation', 'address')
    success_url = reverse_lazy('list')

class PropertyDelete(DeleteView):
    template_name = 'delete.html'
    model = PropertyModel
    success_url = reverse_lazy('list')

class PropertyUpdate(UpdateView):
    template_name = 'update.html'
    model = PropertyModel
    fields = ('property_name', 'school_name', 'content', 'evaluation', 'address')
    success_url = reverse_lazy('list')


class SearchPostView(ListView):
    model = PropertyModel
    template_name = 'search_post.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        ''' lookups = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(evaluation__icontains=query) |
            Q(address__icontains=query)
        ) '''
        lookups = (
            Q(address__icontains=query) |
            Q(property_name__icontains=query) |
            Q(school_name__icontains=query) 
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context