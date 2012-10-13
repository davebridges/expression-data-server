'''This package contains the data structures for the :mod:`researchers`

There is just one model: :class:`~researchers.models.Researcher`
There is also a helper function create_user_profile which creates a new :class:`~researchers.models.Researcher` object for each User object.
'''

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.template.defaultfilters import slugify

class Researcher(models.Model):
    '''This model is for researcher data.
    
    This is this project's UserProfile model and is generated when a new :class:`~django.contrib.auth.models.User`  object is created.'''
    
    user = models.OneToOneField(User)

    current_lab_member = models.BooleanField(help_text = "Is this a current member of this group?")
    
    def __unicode__(self):
        '''The unicode representation for a Personnel object is its full name.'''
        return self.user.get_full_name()

    @models.permalink
    def get_absolute_url(self):
        '''the permalink for a paper detail page is /researcher/1 where user is the researcher id.'''
        return ('researcher-details', [int(self.id)])                 
    

def create_user_profile(sender, instance, created, **kwargs):
    '''This signal generates a new :class:`~researchers.models.Researcher` object for any new :class:`~django.contrib.auth.models.User` objects.'''
    if created:
        Researcher.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
