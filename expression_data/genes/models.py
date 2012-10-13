'''This package assigns the database schema for the :app:`~genes` app.

There is one object, :class:`~genes.models.Gene` which is populated from ENSEMBL data.
'''

from django.db import models

class Gene(models.Model):
    '''This object is for a gene and some associated data regarding this gene.
    
    This is downloaded from ENSEMBL and is currently NCBI M37 for Mus musculus.
    The field names are derived from the downloaded fields.
    I have added two additional fields, created and updated to track our changes.
    The gene name is the primary key, to maintain consistency.'''
    
    name = models.SlugField(max_length=50, help_text="Official Gene Symbol", primary_key=True)
    ensemblID = models.CharField(max_length=30, help_text="ENSEMBL Identification number")
    chromosome = models.CharField(max_length=3, help_text="Chromosome number/name")
    start = models.PositiveIntegerField(help_text="Gene start position (bp)")
    end = models.PositiveIntegerField(help_text="Gene end position (bp)")
    strand = models.IntegerField(help_text="Sense (1) or Antisense(-1)")
    band = models.CharField(max_length=5, blank=True, null=True, help_text="Chromosome band")
    transcript_count = models.PositiveIntegerField(help_text="Transcript count for this gene")
    type = models.CharField(max_length=20, help_text="Gene Type")
    status = models.CharField(max_length=15, help_text="Current Gene Status")

    created = models.DateTimeField(auto_now_add = True, help_text="Created in our database")
    updated = models.DateTimeField(auto_now = True, help_text="Last Updated in our database")
    
    def __unicode__(self):
        '''The unicode representation of a gene is its name'''
        return self.name
        
    @models.permalink
    def get_absolute_url(self):
        '''the permalink for a gene detail page is /gene/<name>'''
        return ('gene-details', [str(self.name)])    