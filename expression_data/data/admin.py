'''
This package has the admin interface for the :mod:`data` app.

All objects have a generic Admin interface.
'''

from django.contrib import admin
from data.models import GeneExperimentData

class GeneExperimentDataAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.GeneExperimentData' objects.'''
    pass
admin.site.register(GeneExperimentData, GeneExperimentDataAdmin)