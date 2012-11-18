'''
This package has the database schemas for the :mod:`experiments` app.

The main kinds of experiments are going to be mRNAseq and microarray data.
In both cases there is "raw" data and analysed data.

This package contains the main :class:`~experiments.models.Experiment` objects as well as the associated metadata objects.
:class:`~experiments.models.Experiment` objects are subclassed into :class:`~experiments.models.mRNASeqExperiment` and :class:`~experiments.models.MicroarrayExperiment` objects.:

* The description of the sample as :class:`~experiments.models.Sample`
* The manipulation of the samples as :class:`~experiments.models.Manipulation`
* The alignment program as :class:`~experiments.models.SequenceAlignmentSoftware` for :class:`~experiments.models.mRNASeqExperiment` objects
* The differential expression program as :class:`~experiments.models.DifferentialExpressionSoftware` for :class:`~experiments.models.mRNASeqExperiment` objects
* The reference genome as :class:`~experiments.models.ReferenceGenomeAssembly` for :class:`~experiments.models.mRNASeqExperiment` objects
* The :class:`~researchers.models.Researcher` objects are defined in the :mod:`researchers` app.
'''

from django.db import models

from researchers.models import Researcher

SPECIES = (
    	('mouse', 'Mus Musculus'),
    	('human', 'Homo Sapiens'),
    	('other', 'Other'),)

class Experiment(models.Model):
    '''
    This base class contains the generic experimental details.
    
    Nothing is stored in these classes, but Experiment objects are subclassed into either
    :class:`~experiments.models.mRNASeqExperiment` or :class:`~experiments.models.MicroarrayExperiment` objects for use.
    The only required field for these objects is the name.
    '''
    
    name = models.CharField(max_length=100, help_text = 'Brief name of the experiment.')
    notes = models.TextField(blank=True, null=True, help_text = "Other notes about the experiment.")
    researchers = models.ManyToManyField(Researcher, blank=True, null=True, help_text = "Who performed this experiment.")
    date_performed = models.DateField(blank=True, null=True, help_text="When was the experiment performed?")
    samples = models.ManyToManyField('Sample', blank=True, null=True, help_text="What are these samples")
    manipulation = models.ManyToManyField('Manipulation', blank=True, null=True, help_text="What was done to these samples?")
    
    #automatic timestamps 
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        '''The unicode representation is the name.'''
        return "%s" % self.name
    
    class Meta:
        '''This is an abstract model.'''
        abstract = True
        
class mRNASeqExperiment(Experiment):
    '''
    These objects are for mRNAseq experiments.
    
    This is a subclass of :class:`experiments.models.Experiment` and uses many of those properties.
    From the base class, name is a required field.
    '''        
          
    alignment_software = models.ForeignKey('SequenceAlignmentSoftware', blank=True, null=True, max_length=10, 
        help_text="Which program was used to align the reads")
    reference_genome = models.ForeignKey('ReferenceGenomeAssembly', blank=True, null=True,
        help_text="What genome assembly were sequences aligned to")
    differential_expression_software = models.ForeignKey('DifferentialExpressionSoftware', blank=True, null=True,
        help_text = "How was differential expression quantified?")
        
    class Meta:
        '''Updated the verbose name of the experiments.'''
        verbose_name_plural = 'mRNA-Seq Experiments'          
    
class MicroArrayExperiment(Experiment):
    '''These objects are for microarray experiments.
    
    This is a subclass of :class:`experiments.models.Experiment` and uses many of those properties.
    From the base class, name is a required field.
    '''
    
    platform = models.CharField(max_length=15, help_text = 'Which chip was used for this microarray, for example GPLxxx')
    differential_expression_software = models.ForeignKey('DifferentialExpressionSoftware', blank=True, null=True,
        help_text = "How was differential expression quantified?")
        
class Software(models.Model):
    '''This model is the base class for software.
   
    The name and version are required fields.
    '''
   
    name = models.CharField(max_length=20, help_text = "Software name.")
    version = models.CharField(max_length=10, help_text = "Software version, or unkown.")
    url = models.URLField(blank=True, null=True, help_text = "Software homepage.")
   
    def __unicode__(self):
        '''The unicode representation is the name followed by the version.'''
        return "%s (%s)" % (self.name, self.version)
       
    class Meta:
        '''This is an abstract model, and the name/version combinations must be unique'''
        abstract = True
        unique_together = ("name", "version")
       
class SequenceAlignmentSoftware(Software):
    '''This model contains the data for the software used in aligning sequencing reads.
   
    This extends the base class :class:`~experiments.models.Software`
    The name and version are required fields.
    '''       

    class Meta:
        '''Updated the verbose name of the software.'''
        verbose_name_plural = 'Sequence Alignment Software'  
    
class DifferentialExpressionSoftware(Software):
    '''This model contains the data for the differential analysis software.
    
    This extends the base class :class:`~experiments.models.Software`
    The name and version are required fields.
    '''
    
    class Meta:
        '''Updated the verbose name of the software.'''
        verbose_name_plural = 'Differential Expression Software'   
       
class ReferenceGenomeAssembly(models.Model):
    '''This object contains details about which reference genome was used.
    
    The source, version and species are required fields.'''
    
    source = models.CharField(max_length=25, help_text="Such as Ensembl, UCSC or NCBI")    
    version = models.CharField(max_length=10, help_text="Which version of the assembly")   
    release_date = models.DateField(blank=True, null=True, help_text = "Release date of this version.")
    url = models.URLField(blank=True, null=True, help_text="Link to the genome assembly.")
    species = models.CharField(choices = SPECIES, max_length=20, help_text="Which species?")

    class Meta:
        '''Updated the verbose name of the assembly.'''
        verbose_name_plural = 'Reference Genome Assemblies'  
    
    def __unicode__(self):
        '''The unicode representation is the source and the version.'''
        return "%s (%s)" % (self.source, self.version)
    
class Sample(models.Model):
    '''This object describes the samples analysed.
    
    The required fields are description, type and species.'''
    
    SAMPLE_TYPES = (
    	('tissue', 'Tissue'),
    	('cells', 'Cells'),
    	('organism', 'Whole Organism'),
    	('in vitro', 'In Vitro'),)
    
    description = models.CharField(max_length=50, help_text="Name for the sample")
    type = models.CharField(choices=SAMPLE_TYPES, max_length=10, help_text="What type are these samples.")
    species = models.CharField(choices=SPECIES, max_length=20, help_text="What species are these samples from?")
    notes = models.TextField(blank=True, null=True, help_text="Additional details about the sample")
    
    def __unicode__(self):
        '''The unicode representation is the description.'''
        return "%s" % self.description
            
class Manipulation(models.Model):
    '''This describes how the samples were differentially manipulated.
    
    The required field is the description'''
    
    description = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        '''The unicode representation is the description.'''
        return "%s" % self.description
    
