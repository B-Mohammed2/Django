from django.http import HttpResponseRedirect
from django.shortcuts import render
from db_app.forms import charities_form # importing the charities model form
from db_app.models import charities_organizations_name # imporiting charity names table

# Create your views here.
def home(request):
    return render(request,"index.html")

def add_charities(request):
    if request.method=='POST': # post method o;y used when data was sent from a form
        form=charities_form(request.POST) # creating a form and storing it in variable form
        if form.is_valid():
            charity_details=charities_organizations_name(charity_name=form.cleaned_data['charities_organizations_name'],
            description=form.cleaned_data['description'],
            contacts=form.cleaned_data['contact_details'],
            email=form.cleaned_data['email']
            )
            charity_details.save() # saving charity details to database
            return HttpResponseRedirect("/thank_you") # roat to html page after saving
    else:
            form=charities_form() # create blank form
    return render(request,"add_charity.html",{"form":form}) # add_charity.html is where the form located    

def thank_you(request):
    return render(request,"thank_you.html")