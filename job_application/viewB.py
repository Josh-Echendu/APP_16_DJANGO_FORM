from django.shortcuts import render
from .forms import ApplicationForm # We used a '.form' becos we had an error 'ModuleNotFoundError: No module named 'forms', so you must use the (.name_of_file) while we are importing a file from a directory i.e the job_application directory'

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
            print(first_name)

        return render(request, "index.html")

# To connect a view function to a url