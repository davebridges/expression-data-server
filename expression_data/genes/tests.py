"""
This package contains the unit tests for the :mod:`~genes` app.

There are tests for the model :class:`~genes.models.Gene`:

* :class:`~researchers.tests.GeneModelTests`
* :class:`~researchers.tests.GeneViewTests`
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from genes.models import Gene

MODELS = [Gene,]

class GeneModelTests(TestCase):
    '''This class tests various aspects of the :class:`~genes.models.Gene` model.'''

    #fixtures = [, ]

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
                
    def test_created_new_gene(self):
        '''This test that a :class:`~genes.models.Gene` can be created.'''
         
        test_gene = Gene(name = "Pikfyve",
        	ensemblID = "ENSMUSG00000025949",
        	chromosome = 1,
        	start = 65186750,
        	end = 65274012,
        	strand = 1,
        	band = "C2",
        	transcript_count = 1,
        	type = "protein_coding",
        	status = "KNOWN")
        test_gene.save()
        self.assertEqual(test_gene.pk, "Pikfyve") #presumes no genes loaded in fixture data
        
    def test_gene_unicode(self):
        '''This tests that the unicode representation of a :class:`~genes.models.Gene` is set as its name.'''               
        
        test_gene = Gene(name = "Pikfyve",
        	ensemblID = "ENSMUSG00000025949",
        	chromosome = 1,
        	start = 65186750,
        	end = 65274012,
        	strand = 1,
        	band = "C2",
        	transcript_count = 1,
        	type = "protein_coding",
        	status = "KNOWN")
        self.assertEqual(test_gene.__unicode__(), "Pikfyve") 
        
    def test_researcher_absolute_url(self):
        '''This tests that the absolute url of a object is **/gene/<name>**.'''
        
        test_gene = Gene(name = "Pikfyve",
        	ensemblID = "ENSMUSG00000025949",
        	chromosome = 1,
        	start = 65186750,
        	end = 65274012,
        	strand = 1,
        	band = "C2",
        	transcript_count = 1,
        	type = "protein_coding",
        	status = "KNOWN")
        self.assertEqual(test_gene.get_absolute_url(), "/gene/Pikfyve")  
        
class GeneViewTests(TestCase):
    '''This class tests the views for :class:`~genes.models.Gene` objects.'''

    fixtures = ['gene_test_fixture',]

    def setUp(self):
        """Instantiate the test client.  Creates a test user."""
        
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')

    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_gene_detail_view(self):
        """This tests the gene-detail view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/gene/Pikfyve')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('gene' in test_response.context)        
        self.assertTemplateUsed(test_response, 'gene-detail.html')
        self.assertEqual(test_response.context['gene'].pk, u'Pikfyve')
        
        #tests a nonfunctional url
        test_response = self.client.get('/gene/Pikfour')
        self.assertEqual(test_response.status_code, 404)
