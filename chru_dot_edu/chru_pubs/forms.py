from django import forms

from tinymce.widgets import TinyMCE

import models 

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=400)
    sender = forms.EmailField()

    # def __str__(self):
    # 	return str(name)
    #cc_myself = forms.BooleanField(required=False)

class PublicationForm(forms.ModelForm):

	#fields
    stub = forms.CharField(widget=TinyMCE(attrs={'cols': 120, 'rows': 4}))

    class Meta:
        model = models.Publication    
        fields = "__all__"