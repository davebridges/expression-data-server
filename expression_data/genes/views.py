"""
This package contains the views for the :mod:`~genes` app.

The only view in this package currently is :class:`~genes.models.GeneDetail`
"""

from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin 

from genes.models import Gene

class GeneDetail(LoginRequiredMixin,DetailView):
    '''This view generates a page with details about a :class:`~genes.models.Gene`.
    
    This view is restricted to logged in users
    This view passes a gene object to the gene-detail.html template.
    '''

    model = Gene
    slug_field = 'name'
    context_object_name = 'gene'
    template_name = 'gene-detail.html'
