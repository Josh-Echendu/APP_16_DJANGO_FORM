from django.shortcuts import render
from .forms import ApplicationForm # We used a '.forms' becos we had an error 'ModuleNotFoundError: No module named 'forms', so you must use the (.name_of_file) while we are importing a file from a directory i.e the job_application directory'
from .models import Form
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        
        # Calling the 'ApplicationForm()' instance from the forms.py file 
        form = ApplicationForm(request.POST)

        # Check form validation
        if form.is_valid():
            # Extracting the values from the html form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            # Store data to the database
            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)

            # Display a message on the screen
            messages.success(request, 'Form submitted successfully.')

            print(first_name)
        return render(request, "index.html")

# store data in a database and display a message