from django import forms
 
# creating a form
class EmailInputForm(forms.Form):
    email_address = forms.EmailField(max_length = 200)

class UploadEmailAddressForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()