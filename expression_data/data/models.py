'''These models control the data saved into the database for a given experiment.

There is a generic base class named Data, which is then further subclassed into specific data models.
'''

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from genes.models import Gene

class BaseData(models.Model):
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
        
class GeneExperimentData(BaseData):                
    '''These data are for gene-level data, aggregated per experiment.
    
    These data can be used with :class:`~experiments.models.mRNASeqExperiment` or :class:`~experiments.models.MicroArrayExperiment` experiments.
    This is an extension of the abstract base model :class:`data.models.BaseData`.
    The fields in this model are based on the columns in the gene_exp.diff from cufflinks.  See http://cufflinks.cbcb.umd.edu/manual.html#cuffdiff_output for more details.
    The required fields are **gene**, **experiment**, **fold_change**, **p_value** and **q_value**.
    '''
    
    locus = models.CharField(max_length=20, blank=True, null=True, help_text="Chromosomal location of this gene.")
    internal_id = models.CharField(max_length=20, blank=True, null=True, help_text="The probe id, or internal identification code for this gene.")
    sample_1 = models.CharField(max_length=20, blank=True, null=True, help_text="The name of the first group in the comparason.")
    sample_2 = models.CharField(max_length=20, blank=True, null=True, help_text="The name of the second group in the comparason.")
    amount_1 = models.DecimalField(max_digits=10, decimal_places=6, help_text="The amount in the first group.")
    amount_2 = models.DecimalField(max_digits=10, decimal_places=6, help_text="The amount in the second group.")
    status = models.CharField(max_length=20, blank=True, null=True, help_text="The status code of the test.")
    fold_change = models.DecimalField(max_digits=6, decimal_places=4, help_text="The log(2) fold change.")
    test_statistic = models.DecimalField(max_digits=6, decimal_places=5, help_text="The value of the test statistic used to compute significance.")
    p_value = models.DecimalField(max_digits=9, decimal_places=8, help_text="Unadjusted p-value.")
    q_value = models.DecimalField(max_digits=9, decimal_places=8, help_text="Multiple Comparason Adjusted p-value (Typically FDR)")
    significant = models.CharField(max_length=3, blank=True, null=True, help_text="Is the q-value < 0.05?")
    
    class Meta:
        '''Updated the verbose name of the datum.'''
        verbose_name_plural = 'Experiment Level Data for a Gene' 
        verbose_name = 'Experiment Level Datum for a Gene' 
    