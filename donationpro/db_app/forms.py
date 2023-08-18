from django import forms
from . models import charities_organizations_name

class charities_form(forms.ModelForm):
    class Meta:
        model=charities_organizations_name
        fields="__all__" # all staitment is to specify displaying all filds from the table
        # lables is to spesify the fild name displayed in the form 
        # e.g "name of the field":"lable in the form",
        labels={
            "charities_organizations_name":"Charity/Organisation Name",
            "description":"Description Of The Organisation ",
            "contact_details":"Contact Details",
            "email":"Organisation Email Address"

        }