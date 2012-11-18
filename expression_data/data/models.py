'''These models control the data saved into the database for a given experiment.

There is a generic base class named Data, which is then further subclassed into specific data models.
'''

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from genes.models import Gene

class Data(models.Model):
    '''This is the abstract base class for all data objects.
    
    This model contains data for a given :class:`~experiments.models.mRNASeqExperiment` or :class:`~experiments.models.MicroArrayExperiment`.
    The experiment is defined by a Generic ForeignKey to one of those two :class:`~experiments.models.Experiment` objects.
    '''

    #These fields control the foreignkey to the experiment.
    experiment_type_choices = models.Q(app_label = 'experiments', model = 'mrnaseqexperiment') | models.Q(app_label = 'experiments', model = 'microarrayexperiment') 
    
    experiment_type = models.ForeignKey(ContentType, limit_choices_to = experiment_type_choices, help_text="Experiment Type")
    experiment_id = models.PositiveIntegerField()
    experiment = generic.GenericForeignKey('experiment_type', 'experiment_id')

    gene = models.ForeignKey(Gene, help_text="The gene for these data.")
    
    def __unicode__(self):
        '''The unicode representation is the name.'''
        return "%s" % self.gene
    
    class Meta:
        '''This is an abstract model.'''
        abstract = True        
