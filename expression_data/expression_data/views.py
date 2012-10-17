'''This package has the generic views.

Currently there is just the :class:`expression_data.views.SearchView` which is used to search for :class:`~genes.models.Gene`
'''

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

from expression_data.forms import SearchForm
from genes.models import Gene

class SearchView(FormView):
    '''This view takes a gene query and directs the user to the detail page for that gene.
    
    Currently only correct, unique, capitalized gene names are redirected.
    '''

    template_name = 'search.html'
    form_class = SearchForm
    
    def get_success_url(self, *args, **kwargs):
        '''This function redirects the user to the **gene-detail** page in the case of a match'''
        query = self.request.POST['gene']
        try:
            Gene.objects.get(name=query)
            return reverse_lazy('gene-details', kwargs={'slug': query})
        except Gene.DoesNotExist:
            raise Http404