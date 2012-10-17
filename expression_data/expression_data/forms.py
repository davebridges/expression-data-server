'''This package contains generic forms.

The only form class defined is the search form used in :class:`expression_data.forms.SearchView`.
'''

from django import forms

class SearchForm(forms.Form):
    '''This form is for keyword searches.'''
    
    gene = forms.CharField(max_length=100, help_text="First letter must be capitalized.")