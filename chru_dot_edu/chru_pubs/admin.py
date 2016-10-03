from django.contrib import admin
from django import forms
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required
from forms import PublicationForm
import models


class PublicationAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PublicationAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'stub':
            formfield.widget = forms.Textarea(attrs={'cols': 120, 'rows': 4})
        #elif db_field.name == 'authors':
        #    formfield.widget = forms.MultipleChoiceField(size="10")
        return formfield

    def get_urls(self):
        urls = super(PublicationAdmin, self).get_urls()
        my_urls = [
            url(r'^pubmed/(?P<pubmedid>\w+)/$', self.pubmedid,name="pubmed"),
        ]
        return my_urls + urls

    #@login_required
    def pubmedid(self,request,pubmedid):
        # custom view which should return an HttpResponse
        print "reached pubmed view, query : " + pubmedid
        pass        

    #def __init__(self, db_field, **kwargs):
    #    self.fields['authors'].widget.attrs['size']='10'

    class Media:
        js = ('/js/tinymce/tinymce.min.js', )

    form = PublicationForm
    list_display = ('pubmedid', 'pubdate')



class PersonAdmin(admin.ModelAdmin):

    #list_display = ('full_name','uwnetid')
    #def get_urls(self)
    #def my_view(self, request):
    # class Media:
    #   js = ('path to js',)
    list_display = ('full_name', 'employment_type')	

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PersonAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'interests':
            formfield.widget = forms.Textarea(attrs={'cols': 120, 'rows': 4})
        elif db_field.name == 'title':
            formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 4})
        elif db_field.name == 'education':
            formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 4})            
        elif db_field.name == 'honors':
            formfield.widget = forms.Textarea(attrs={'cols': 80, 'rows': 4})            
        return formfield

    # fieldsets = (

    #   (),
    # )

admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Study)
admin.site.register(models.Publication, PublicationAdmin)
