from django.shortcuts import render
from django.views import View
from .models import*
from django.contrib import messages
# Create your views here.




class HomeView (View):
    """ Main view  """
    
    templates_name = 'index.html'
    
    thefacs = Thefac.objects.select_related ('client','Eng_par').all()
    
    context = {
        'thefacs': thefacs
    }
    

    
    def get (self, request, *args, **kwargs):
        return render (request, self.templates_name, self.context)
    
    def post (self, request, *args, **kwargs):
        
        return render (request, self.templates_name, self.context)
    

class AddClientView (View):
    """add new client """
    templates_name = 'add_client.html'
    
    
    def get (self, request, *args, **kwargs):
        return render (request, self.templates_name)
    
    def post (self, request, *args, **kwargs):
        
        
        data = {
            'name': request.POST.get ('name'),
            'email': request.POST.get ('email'),
            'telephone':request.POST.get ('telephone'),
            'Adresse': request.POST.get ('adresse'),
            'sexe': request.POST.get ('sexe'),
            'Age':request.POST.get ('age'),
            'ville': request.POST.get('ville'),
            'vode_postal': request.POST.get ('code_postal'),
            'eng_par':request.user
        }
        
        try:
            created = Client.objects.create (**data)
            
            if created:
                messages.success (request, "Client registered successfuly.")
                
            else :
                messages.error (request, "Sorry, please try again the sent data is corrupt .")
                
        
        except Exception as e:
            messages.error (request, f"Sorry our system is detecting the  following issues  {e}.")
            
        return render (request, self.templates_name)
    
        