from django import forms

from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=250, help_text='', required=True,
                    widget=forms.TextInput(
                        attrs= {"class":"form-control", "id":"username", 'type':"text", "placeholder":"username", "data-sb-validations":"required"}
                        )
                    )
    
    first_name = forms.CharField(label="First Name", max_length=250, help_text='', required=True,
                    widget=forms.TextInput(
                        attrs= {"class":"form-control", "id":"first_name", 'type':"text", "placeholder":"first_name", "data-sb-validations":"required"}
                        )
                    )

    last_name = forms.CharField(label="Last Name", max_length=250, help_text='', required=True,
                    widget=forms.TextInput(
                        attrs= {"class":"form-control", "id":" last_name", 'type':"text", "placeholder":" last_name", "data-sb-validations":"required"}
                        )
                    )
    
    email = forms.CharField(label="Email ", max_length=250, help_text='', required=True,
                    widget=forms.TextInput(
                        attrs= {"class":"form-control", "id":" email", 'type':"email", "placeholder":" email", "data-sb-validations":"required"}
                        )
                    )
    
    password = forms.CharField(label="Password", max_length=250, help_text='', required=True,
                    widget=forms.TextInput(
                        attrs= {"class":"form-control", "id":"   password", 'type':"password", "placeholder":"   password", "data-sb-validations":"required"}
                        )
                    )
    
    confirm_password = forms.CharField(label="Confirm Password Name", max_length=250, help_text='', required=True,
                    widget=forms.TextInput(
                        attrs= {"class":"form-control", "id":"confirm_password", 'type':"password", "placeholder":"confirm_password", "data-sb-validations":"required"}
                        )
                    )
    
    
   
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')