'''This package contains the views for the :mod:`researchers`  app.

Currently there is a detail view of :class:`~researchers.models.Researcher` objects
'''

from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin 

from researchers.models import Researcher

class ResearcherDetail(LoginRequiredMixin,DetailView):
    '''This view generates a page with details about a :class:`~researchers.models.Researcher`.
    
    This view is restricted to logged in users
    This view passes a researcher object to the researcher-detail.html template.
    '''

    model = Researcher
    context_object_name = 'researcher'
    template_name = 'researcher-detail.html'
    
    