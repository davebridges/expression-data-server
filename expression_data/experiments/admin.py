'''
This package has the admin interface for the :mod:`experiments` app.

All objects have a generic Admin interface.
'''

from django.contrib import admin
from experiments.models import mRNASeqExperiment, SequenceAlignmentSoftware, DifferentialExpressionSoftware, ReferenceGenomeAssembly, Sample, Manipulation, MicroArrayExperiment

class mRNASeqExperimentAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.mRNASeqExperiment' objects.'''
    pass
admin.site.register(mRNASeqExperiment, mRNASeqExperimentAdmin)

class MicroArrayExperimentAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.MicroArrayExperiment' objects.'''
    pass
admin.site.register(MicroArrayExperiment, MicroArrayExperimentAdmin)

class SequenceAlignmentSoftwareAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.SequenceAlignmentSoftware' objects.'''
    pass
admin.site.register(SequenceAlignmentSoftware, SequenceAlignmentSoftwareAdmin)

class DifferentialExpressionSoftwareAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.DifferentialExpressionSoftware' objects.'''
    pass
admin.site.register(DifferentialExpressionSoftware, DifferentialExpressionSoftwareAdmin)

class ReferenceGenomeAssemblyAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.ReferenceGenomeAssembly' objects.'''
    pass
admin.site.register(ReferenceGenomeAssembly, ReferenceGenomeAssemblyAdmin)

class SampleAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.Sample' objects.'''
    pass
admin.site.register(Sample, SampleAdmin)

class ManipulationAdmin(admin.ModelAdmin):
    '''Generic admin interface for :class:`~experiments.models.Manipulation' objects.'''
    pass
admin.site.register(Manipulation, ManipulationAdmin)


    
