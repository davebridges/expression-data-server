"""
This package contains the unit tests for the :mod:`~experiments` app.

There are tests for the models in this app including:

* :class:`~experiments.models.mRNASeqExperiment` as :class:`~experiments.models.mRNASeqExperimentModelTests`
* :class:`~experiments.models.Sample` as :class:`~experiments.models.SampletModelTests`
* :class:`~experiments.models.Manipulation` as :class:`~experiments.models.ManipulationModelTests`
* :class:`~experiments.models.SequenceAlignmentSoftware` as :class:`~experiments.models.SequenceAlignmentSoftwareModelTests`
* :class:`~experiments.models.DifferentialExpressionSoftware` as :class:`~experiments.models.DifferentialExpressionSoftwareModelTests`
* :class:`~experiments.models.ReferenceGenomeAssembly` as :class:`~experiments.models.ReferenceGenomeAssembly`

There are no views for these objects yet so no ViewTests

There are no tests for :class:`~experiments.models.Experiment` or :class:`~experiments.models.Software` as these are abstract base classes and not called directly.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from experiments.models import mRNASeqExperiment, Sample, Manipulation, SequenceAlignmentSoftware, DifferentialExpressionSoftware, ReferenceGenomeAssembly

MODELS = [mRNASeqExperiment, Sample, Manipulation, SequenceAlignmentSoftware, DifferentialExpressionSoftware, ReferenceGenomeAssembly
,]

class GeneralTestCase(TestCase):
    '''This base class defines both the setUp and tearDown functions for a TestCase.'''
    
    def setUp(self):
        '''Instantiate the test client.  Creates a test user.'''
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.first_name = "Joe"
        self.test_user.last_name = "Blow"
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
    
    def tearDown(self):
        '''Depopulate created model instances from test database.'''
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

class mRNASeqExperimentModelTests(GeneralTestCase):
    '''This class tests various aspects of the :class:`~experiments.models.mRNASeqExperiment` model.'''
                
    def test_created_new_mrnaseq_experiment_minimal(self):
        '''This test that a :class:`~experiments.models.mRNASeqExperiment` can be created.'''
         
        test_experiment = mRNASeqExperiment(name = "Test Experiment")
        test_experiment.save()
        self.assertEqual(test_experiment.pk, 1) #presumes no genes loaded in fixture data
        
    def test_mraneseq_experiment_unicode(self):
        '''This tests that the unicode representation of an :class:`~experiments.models.mRNASeqExperiment` is set as its name.'''               
        
        test_experiment = mRNASeqExperiment(name = "Test Experiment")
        test_experiment.save()
        self.assertEqual(test_experiment.__unicode__(), "Test Experiment")         
        
class SampleModelTests(GeneralTestCase):
    '''This class tests various aspects of the :class:`~experiments.models.Sample` model.'''
                
    def test_created_new_sample_minimal(self):
        '''This test that a :class:`~experiments.models.Sample` can be created.'''
         
        test_sample = Sample(description = "Test Sample", type="tissue", species="mouse")
        test_sample.save()
        self.assertEqual(test_sample.pk, 1) #presumes no genes loaded in fixture data
        
    def test_sample_unicode(self):
        '''This tests that the unicode representation of an :class:`~experiments.models.Sample` is set as its description.'''               
        
        test_sample = Sample(description = "Test Sample", type="tissue", species="mouse")
        test_sample.save()
        self.assertEqual(test_sample.__unicode__(), "Test Sample") 
        
class ManipulationModelTests(GeneralTestCase):
    '''This class tests various aspects of the :class:`~experiments.models.Manipulation` model.'''
                
    def test_created_new_manipulation_minimal(self):
        '''This test that a :class:`~experiments.models.Manipulation` can be created.'''
         
        test_manipulation = Manipulation(description = "Test Manipulation")
        test_manipulation.save()
        self.assertEqual(test_manipulation.pk, 1) #presumes no genes loaded in fixture data
        
    def test_manipulation_unicode(self):
        '''This tests that the unicode representation of an :class:`~experiments.models.Manipulation` is set as its description.'''               
        
        test_manipulation = Manipulation(description = "Test Manipulation")
        test_manipulation.save()
        self.assertEqual(test_manipulation.__unicode__(), "Test Manipulation")                
       
class SequenceAlignmentSoftwareModelTests(GeneralTestCase):
    '''This class tests various aspects of the :class:`~experiments.models.SequenceAlignmentSoftware` model.'''
                
    def test_created_new_align_software_minimal(self):
        '''This test that a :class:`~experiments.models.SequenceAlignmentSoftware` can be created.'''
         
        test_software = SequenceAlignmentSoftware(name = "Test Software", version="1.0.1")
        test_software.save()
        self.assertEqual(test_software.pk, 1) #presumes no genes loaded in fixture data
        
    def test_align_software_unicode(self):
        '''This tests that the unicode representation of an :class:`~experiments.models.SequenceAlignmentSoftware` is set as its description.'''               
        
        test_software = SequenceAlignmentSoftware(name = "Test Software", version="1.0.1")
        test_software.save()
        self.assertEqual(test_software.__unicode__(), "Test Software (1.0.1)")        
        
class DifferentialExpressionSoftwareModelTests(GeneralTestCase):
    '''This class tests various aspects of the :class:`~experiments.models.DifferentialExpressionSoftware` model.'''
                
    def test_created_new_de_software_minimal(self):
        '''This test that a :class:`~experiments.models.DifferentialExpressionSoftware` can be created.'''
         
        test_software = DifferentialExpressionSoftware(name = "Test Software", version="1.0.1")
        test_software.save()
        self.assertEqual(test_software.pk, 1) #presumes no genes loaded in fixture data
        
    def test_de_software_unicode(self):
        '''This tests that the unicode representation of an :class:`~experiments.models.DifferentialExpressionSoftware` is set as its description.'''               
        
        test_software = DifferentialExpressionSoftware(name = "Test Software", version="1.0.1")
        test_software.save()
        self.assertEqual(test_software.__unicode__(), "Test Software (1.0.1)")   
              
class ReferenceGenomeAssemblyModelTests(GeneralTestCase):
    '''This class tests various aspects of the :class:`~experiments.models.ReferenceGenomeAssembly` model.'''
                
    def test_assembly_minimal(self):
        '''This test that a :class:`~experiments.models.ReferenceGenomeAssembly` can be created.'''
         
        test_assembly = ReferenceGenomeAssembly(source = "Ensembl", version="37.1", species="mouse")
        test_assembly.save()
        self.assertEqual(test_assembly.pk, 1) #presumes no genes loaded in fixture data
        
    def test_assembly_unicode(self):
        '''This tests that the unicode representation of an :class:`~experiments.models.ReferenceGenomeAssembly` is set as its description.'''               
        
        test_assembly = ReferenceGenomeAssembly(source = "Ensembl", version="37.1", species="mouse")
        test_assembly.save()
        self.assertEqual(test_assembly.__unicode__(), "Ensembl (37.1)")               