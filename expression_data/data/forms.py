'''This package controls forms relevant to the :mod:`data` app.

'''

from django import forms

from experiments.models import mRNASeqExperiment

class CufflinksImportForm(forms.Form):
    '''This form is used as the input for a :class:`~data.views.CufflinksImportFormView`.'''
    
    experiment = forms.IntegerField(help_text="Enter the identification number for the experiment.")
    uploaded_file = forms.FileField(help_text="Upload a genes_exp.diff file")
    
    def clean_experiment(self):
        '''This function checks that the entered experiment is a valid :class:`~data.models.mRNASeqExperiment`.'''
        
        data = self.cleaned_data['experiment']
        try: 
            mRNASeqExperiment.objects.get(pk=data)
        except mRNASeqExperiment.DoesNotExist:
            raise forms.ValidationError("Invalid Experiment ID.")
        return data