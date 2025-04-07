from django.shortcuts import render
from django.views import View
from .models import*
from django.contrib import messages
# Create your views here.

from django.db import transaction


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
            'Name': request.POST.get ('name'),
            'Email': request.POST.get ('email'),
            'Telephone':request.POST.get ('telephone'),
            'Adresse': request.POST.get ('adresse'),
            'Sexe': request.POST.get ('sexe'),
            'Age':request.POST.get ('age'),
            'Ville': request.POST.get('ville'),
            'Code_postal': request.POST.get ('code_postal'),
            'Eng_par':request.user
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
    
    
    

class AddThefacView (View):
    
    """ add a new thefac view """
    
    templates_name = 'add_thefac.html'
    
    client = Client.objects.select_related('Eng_par').all()
    
    context = {
        'clients ': client
    }
    
    
    def get (self, request, *args, **kwargs):
        return render (request, self.templates_name, self.context)
        
    @transaction.atomic   
    def post (self, request, *args, **kwargs):
        
        print (request.POST)
        
        items = []
        
        try:
            
            client = request.POST.get ('client')
            
            type = request.POST.get ('thefac_type')
            
            articles = request.POST.getlist ('article')
            
            qties = request.POST.getlist('qty')
            
            units = request.POST.getlist('unit')
            
            total_a = request.POST.getlist('total-a')
            
            total = request.POST.get('total')
            
            commentaires = request.POST.get ('commentaires')
            
            
            thefac_object = {
                'client_id': client,
                'Eng_par'  :request.user,
                'Total'   : total,
                'Thefac_type': type,
                'Commentaires':  commentaires
            }
            
            
            thefac = Thefac.objects.create(**thefac_object)
            
            for index,  article in enumerate (articles):
                
                data= Article(
                    thefac_id = thefac.id,
                    Name = article,
                    Quantity=qties[index],
                    Prix_unitaire=[index],
                    Total=total_a[index],
                    
                )
                
                items.append (data)
                
            created = Article.objects.bulk_create (items)
            
            if created:
                messages.success (request, "Data saved successfully.")
                
            else:
                
                messages.error (request, "Sorry please try again the sent data is corrupt.")
                
        except  Exception as e :
            
            messages.error(request, f"Sorry the following error has occured {e}.")
         
        return render (request, self.templates_name, self.context)