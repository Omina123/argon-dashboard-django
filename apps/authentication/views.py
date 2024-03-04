# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import pandas as pd
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,A4

# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import*
from apps.home.views import*
import time



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
from .forms import*

# Load the machine learning model.
#model = joblib.load('anthrax_prediction_model.pkl')

dataset = [
    ('sudden death', 'Dispose of dead animals properly.', 1),
    ('death', 'Dispose of dead animals properly.', 1),

    ('difficulty in breathing', 'Avoid grazing your goats in areas where anthrax is known to occur.', 1),
    ('high fever', 'Vaccinate your goats against anthrax.', 1),
    ('fever', 'It is crucial to ensure the health and safety of your goats by considering anthrax vaccination. Anthrax poses a serious threat to livestock, and preventive measures are essential. Consult with a veterinarian to discuss an appropriate vaccination schedule tailored to your goats needs. Timely immunization can effectively safeguard your herd against anthrax infections, preventing potential outbreaks and ensuring the overall well-being of your animals. Prioritize this preventive measure to promote a healthy and thriving goat population on your farm.', 1),

    ('loss of appetite', 'Vaccinate your goats against anthrax.', 1),
    ('swelling', 'Vaccinate your goats against anthrax.', 1),
    ('weakness', 'Wear gloves and other protective gear when handling dead animals.', 1),
    ('nose discharge and mouth', 'Wear gloves and other protective gear when handling dead animals.', 1),
    ('Bloody diarrhea', 'Wear gloves and other protective gear when handling dead animals.', 1),
    ('no discharge and mouth', 'Continue monitoring your goat for anthrax infections. Also, visit the following link for more information: https://www.msdvetmanual.com/generalized-conditions/anthrax/anthrax-in-animals', 0),
    ('normal breathing', 'If you are in a situation where anthrax exposure is suspected, it is important to follow guidance from public health authorities and emergency services. They can provide information on appropriate actions to take and any necessary preventive measures.', 0),
]

# In views.py

import joblib

# Load the trained model
#model = joblib.load('recommendation_model.joblib')
# views.py


# Load the trained model
model = joblib.load('omina_model.joblib')
# def omina(request):

@login_required
# views.py

def get_reco(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']

            # Get the currently logged-in user and set it as the farmer
            farmer = request.user
            

            # Use the trained model to make a recommendation
            symptoms_data = pd.DataFrame({'symptoms': [symptoms], 'diagnosis': [1]})  # Assuming diagnosis is 1, you may need to adjust this
            recommendation = model.predict(symptoms_data['symptoms'])[0]

            # Save the recommendation to the database
            AnthraxSymptom.objects.create(
                farmer=farmer,
                symptoms=symptoms,
                recommendation=recommendation
            )
            time.sleep(10)

            # Redirect to a page showing the saved recommendations
            return render(request, 'home/recommendation.html', {'symptoms': symptoms, 'recommendation': recommendation})

    else:
        form = SymptomForm()

    return render(request, 'home/re.html', {'form': form})



def get_recommendation(symptom):
    # Find the recommendation associated with the provided symptom in the dataset
    for s, recommendation, diagnosis in dataset:
        if symptom == s:
            return recommendation

    # If the symptom is not found, return a default message or handle it as needed.
    return 'Provided symptom does not have a recommendation for my knolwedge. Seek professional advice for accurate diagnosis and tailored guidance on addressing your specific concern.'


     
def get_recommendation_view(request):
    if request.method == 'POST':
        symptom = request.POST.get('symptom', '')
        recommendation = get_recommendation(symptom)

        # Save the recommendation in the database
        AnthraxSymptom.objects.create(symptom=symptom, recommendation=recommendation)
        time.sleep(10)

        return render(request, 'user.html', {'symptom': symptom, 'recommendation': recommendation})
    else:
        return render(request, 'symptom_selector.html')
# @login_required(login_url="/login/farmer")
def homei(request):
    title = 'Welcome: '.upper()
    welcome =  'Welcome to the Anthrax Recommendation System, your trusted guide for informed decisions on anthrax prevention, diagnosis, and treatment. Explore personalized recommendations to safeguard your health and well-being,  click on  below to get recommendation for anthrax.'.upper()
    context = {
        "title": title,
        "welcome": welcome
    }
    return render(request, "home/st.html", context)
import logging

logger = logging.getLogger(__name__)
def enter(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            symptom_list = [symptoms.strip() for symptoms in symptoms.split(',')]
            
            recommendations = [get_recommendation(symptoms) for symptoms in symptom_list]

            # Save symptoms and recommendations to the database
            farmer= request.user.username
          
            data = []
            for symptom, recommendation in zip(symptom_list, recommendations):
                AnthraxSymptom.objects.create(farmer=farmer,symptoms=symptoms, recommendation=recommendation)
            #loading_indicator = True

            # Wait for 10 seconds
            time.sleep(10)

            # Hide the loading indicator
            loading_indicator = False
            return render(request, 'home/bas.html', {'recommendations': recommendations})
    else:
        form = SymptomForm()
    return render(request, 'home/ko.html', {'form': form})
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = ""

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            
            print(logger.debug(f"Received login attempt for username: {username}"))

            user = authenticate(username=username, password=password)
            if user is not None:
                logger.debug("Authentication successful")
                login(request, user)
                if user.role == 'farmer':
                    time.sleep(5)
                    return redirect('homei')
               
                elif user.role == 'agrics_officer':
                 return redirect('index')
                
                else:
                    logger.debug("Authentication failed")
                    msg = 'Authentication failed due invalid password or username'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/log.html", {"form": form, "msg": msg})
def fogot_password(request):
    form=  FogotForm
    return render(request, 'accounts/forgot_pswd.html',{'form':form})
def register_user(request):
    success = False
    msg = None

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created - please <a href="/login_view">login</a>.'
            success = True
            time.sleep(5)
            return redirect('login_view')
        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(request, "accounts/reg.html", {"form": form, "msg": msg, "success": success})
# def delete (request, pk):
#     queryset=AnthraxSymptom.objects.filter(id=pk)
#     if request.method=="POST":
#         queryset.delete()
#     return redirect(request,"home/delete.html",{'quersyet':queryset})

   
def delete(request, pk):
    dr =  'deteleted succeffully'.upper()# variable that contained a detelet messsage after succeflly deleting reccomendations
    queryset = AnthraxSymptom.objects.filter(id=pk)#getting data from the history daytabase under the table called anthraxSymptoms

    if request.method == 'POST': #a aondition that the validity of the request
        queryset.delete() # a method that will carry on delete function
        messages.success(request, dr  )
        return redirect('history')
    return render(request, "home/delete.html",{'queryset':queryset,'dr':dr}) 
def history (request):
    title=" below is our previous reccomdation ".upper()
    queryset= AnthraxSymptom.objects.all
    context={
        'title':title,
        'queryset':queryset
    }
    return render(request, "home/history.html",context)
def kevo(request):
    queryset= AnthraxSymptom.objects.all
    context= {
        'queryset':queryset
    }
    return render(request, 'home/kevo.html', context)
def hire (request, pk):
    querset= AnthraxSymptom.objects.get(id=pk)
    context={
        'querset':querset
    }
    return render(request, 'home/hire.html',context)
def pdf(request, pk):
    case_data = AnthraxSymptom.objects.get(id=pk)  # Assuming you want to get the first case from the database
    
    # Create a PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Anthrax_recomendations.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Define styles for the PDF content
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'])
    custom_style.spaceBefore = 20
    custom_style.spaceAfter = 20

    # Create the content for the case report
    content = [
        Paragraph("\t\t\t\tFirm: \tMAKONGEN AGRICULTURAL FIRM "),
                Paragraph("\t\t\tEmail: \t Makongeni@gmail.com "),
                        Paragraph("\t\t\t\tTell: \t +254 759 975 197 "),
                        Paragraph("\t\t\t\t Post: \t P.O BOX 2000, Nairobi "),
                        Paragraph("\t\t\t\t Farmer: {}".format(request.user.username), custom_style),
                        #Paragraph("\t\t\t\t firstname: {}".format(USER.first_name), custom_style),
                        
         

        Paragraph("SYMPTOM: {}".format(case_data.symptoms), custom_style),
      
                       Paragraph("\t\t\t\t RECOMMENDATION "),

        Paragraph(" {}".format(case_data.recommendation), custom_style),
         Paragraph("Farmer signature:   ......................", custom_style),
        Paragraph("DATE:   ......................", custom_style),

       
        Paragraph("Hod signature:   ......................", custom_style),
        Paragraph("DATE:   ......................", custom_style),
        Paragraph("", custom_style),
        Paragraph("", custom_style),
        Paragraph("", custom_style),
      



    ]

    # Build the PDF document
    doc.build(content)

    return response