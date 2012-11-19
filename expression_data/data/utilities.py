'''This package contains utility functions for the :mod:`data` app.

These functions import data from a variety of tables into the database.
'''

import csv

from data.models import GeneExperimentData
from experiments.models import mRNASeqExperiment
from genes.models import Gene

def cufflinks_gene_diff_import(experiment_id, filename):
    '''This function imports the data from a gene_exp.diff into :class:`~data.models.GeneExperimentData` objects.
    
    This function requires a valid experiment_id and a file.
    '''
    experiment = mRNASeqExperiment.objects.get(pk=experiment_id)
    new_genes = 0
    updated_genes =0
    with open(filename, 'r') as inputfile:
        for row in csv.DictReader(inputfile, delimiter='\t'):
            try: 
                datum = GeneExperimentData(
                     experiment=experiment,
        			 gene=Gene.objects.get(pk=row['gene']),
        			 fold_change = row['log2(fold_change)'],
        			 p_value = row['p_value'],
        			 q_value = row['q_value'],
        			 locus = row['locus'],
        			 internal_id = row['test_id'],
        			 sample_1 = row['sample_1'],
        			 sample_2 = row['sample_2'],
        			 amount_1 = row['value_1'],
        			 amount_2 = row['value_2'],
        			 status = row['status'],
        			 test_statistic = row['test_stat'],
        			 significant = row['significant'])
                datum.save()
                updated_genes += 1
            except Gene.DoesNotExist:
                #create a new gene with that name
                new_gene = Gene(name=row['gene'])
                new_gene.save()
                datum = GeneExperimentData(
                     experiment=experiment,
        			 gene=new_gene,
        			 fold_change = row['log2(fold_change)'],
        			 p_value = row['p_value'],
        			 q_value = row['q_value'],
        			 locus = row['locus'],
        			 internal_id = row['test_id'],
        			 sample_1 = row['sample_1'],
        			 sample_2 = row['sample_2'],
        			 amount_1 = row['value_1'],
        			 amount_2 = row['value_2'],
        			 status = row['status'],
        			 test_statistic = row['test_stat'],
        			 significant = row['significant'])
                datum.save()
                new_genes +=1
    return "Added %i measurements and created %i new genes." %(updated_genes+new_genes, new_genes)              
                