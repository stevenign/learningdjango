from django.shortcuts import render, get_object_or_404
from .models import References
from django.views.generic import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy


def references_list(request, tag_slug=None):
    referencess = References.published.all()
    return render(request,
                  'references/references/list.html',
                  {'referencess' : referencess})


def references_detail(request, year, month, day, references):
    references = get_object_or_404(References, titleRf=references, statusRf='published',
                                publish__year=year, publish__month=month, publish__day=day)
    
    

    return render(request, 'references/references/detail.html', {'references' : references,})

class ReferencesCreateView(CreateView):
    model = References
    fields = ['titleRf', 'descriptionRf', 'linkRf','authorRf','createdRf','updatedRf','statusRf']
    
class ReferencesUpdateView(UpdateView):
    model = References
    fields = ['titleRf', 'descriptionRf', 'linkRf','authorRf','createdRf','updatedRf','statusRf']
    
class ReferencesDeleteView(DeleteView):
    model = References
    success_url = reverse_lazy('references:references_list')