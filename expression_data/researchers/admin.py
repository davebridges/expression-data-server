'''This package details the administrative interface for the :mod:`researchers` app.

Since :class:`~researchers.models.Researcher` objects are not created directly, but are instead created during a :class:`~django.contrib.auth.models.User` object generation, there is no direct admin interface for :class:`~researchers.models.Researcher` objects.
:class:`~django.contrib.auth.models.User` objects have an inline set up by :class:`~researchers.admin.ResearcherInline`.
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from researchers.models import Researcher

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class ResearcherInline(admin.StackedInline):
    ''':class:`~researchers.models.Researcher` objects are controlled via an inline to :class:`~researchers.models.UserAdmin`.
    '''
    model = Researcher
    can_delete = False
    verbose_name_plural = 'researcher'

# Define a new User admin
class UserAdmin(UserAdmin):
    '''Over-rides UserAdmin to add the :class:`~researchers.models.ResearcherInline`.'''
    inlines = (ResearcherInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)