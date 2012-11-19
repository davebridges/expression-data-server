'''This package controls views relevant to the :mod:`data` app.

'''

from django.views.generic.edit import FormView

from data.forms import CufflinksImportForm

class CufflinksImportFormView(FormView):
    '''This view generates and processes the data from a cufflinks genes_exp.diff file.
    
    '''
    form_class = CufflinksImportForm
    template_name = "import_form.html"
    success_url = "/admin/data"
    
    def form_valid(self, form):
        '''This function, which is passed only when the form has been validated writes the data from the file into the database.'''

        import os

        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        from django.conf import settings
        
        from data.utilities import cufflinks_gene_diff_import

        #temporarily saves the file to the disk
        data = form.cleaned_data['uploaded_file']
        path = default_storage.save('tmp/genes_exp.diff', ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        #saves the records to the database.
        import_result = cufflinks_gene_diff_import(form.cleaned_data['experiment'], tmp_file)
        #deletes the file.
        path = default_storage.delete('tmp/genes_exp.diff')
        return super(CufflinksImportFormView, self).form_valid(form)
    
    