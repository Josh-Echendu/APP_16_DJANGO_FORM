from django.db import models

# Create your data models here.
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # Add a magic method: This magic method 'def __str__(self):' defines what is to be printed when a print function is used
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"
    
#    django-admin startproject mysite .: Set up a project directry called 'mysite'
#    python manage.py startapp job_application: Create your app
#    python manage.py runserver: Run your code
#    python manage.py makemigrations: Create migrations i.e connecting your database model to a DBMS
#    python manage.py migrate: To apply the codes generated by 'python manage.py makemigrations' to the DBMS 