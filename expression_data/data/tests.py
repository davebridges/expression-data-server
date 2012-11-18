"""
This package contains the unit tests for the :mod:`data` app.


There are tests for each model in this app.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from data.models import GeneExperimentData
from experiments.models import mRNASeqExperiment
from genes.models import Gene
MODELS = [GeneExperimentData,]

class GeneExperimentDataTests(TestCase):
    '''This class tests various aspects of the :class:`~data.models.GeneExperimentData` model.'''

    fixtures = ['experiment_test_fixture', 'gene_test_fixture', ]

    def setUp(self):
        '''Instantiate the test client.  Creates a test user.'''
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
    
    def tearDown(self):
        '''Depopulate created model instances from test database.'''
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
                
    def test_create_new_gene_experiment_datum_minimum(self):
        '''This test creates a :class:`~data.models.GeneExperimentData` with the required information only.'''

        test_datum = GeneExperimentData(experiment=mRNASeqExperiment.objects.get(pk=1),
        	gene=Gene.objects.get(pk='Pikfyve'),
        	fold_change = 0.419048218,
        	p_value = 0.110512214,
        	q_value = 0.995959851) 
        test_datum.save()
        self.assertEqual(test_datum.pk, 1) #presumes no objects loaded in fixture data
        
    def test_create_new_gene_experiment_datum_all(self):
        '''This test creates a :class:`~data.models.GeneExperimentData` with all information entered.'''

        test_datum = GeneExperimentData(experiment=mRNASeqExperiment.objects.get(pk=1),
        	gene=Gene.objects.get(pk='Pikfyve'),
        	fold_change = 0.419048218,
        	p_value = 0.110512214,
        	q_value = 0.995959851,
        	locus = '1:3054232-3054733',
        	internal_id = 'XLOC_000001',
        	sample_1 = 'Control',
        	sample_2 = 'Treated',
        	amount_1 = 0.0778978,
        	amount_2 = 0.0881688,
        	status = 'OK',
        	test_statistic = -0.0754818,
        	significant = 'no') 
        test_datum.save()
        self.assertEqual(test_datum.pk, 1) #presumes one model loaded in fixture data       
        
    def test_gene_experiment_datum_unicode(self):
        '''This tests the unicode representation of a :class:`~data.models.GeneExperimentData`.'''

        test_datum = GeneExperimentData(experiment=mRNASeqExperiment.objects.get(pk=1),
        	gene=Gene.objects.get(pk='Pikfyve'),
        	fold_change = 0.419048218,
        	p_value = 0.110512214,
        	q_value = 0.995959851) 
        self.assertEqual(test_datum.__unicode__(), "Pikfyve")