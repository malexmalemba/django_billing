from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client (models.Model):
    
    """
    name : Client model definition
    """
    SEX_TYPES=(
        ('M','Masculin'),
        ('F','Feminin '),
    )
    
    Name = models.CharField (max_length=132)
    
    Email = models.EmailField ()
    
    Telephone = models.CharField (max_length=132)
    
    Adresse = models.CharField (max_length=64)
    
    Sexe = models.CharField (max_length=1,choices=SEX_TYPES)
    
    Age = models.CharField (max_length=12)
    
    Ville = models.CharField (max_length=32)
    
    Code_postal = models.CharField (max_length=16)
    
    Date = models.DateTimeField (auto_now_add=True)
    
    Eng_par = models.ForeignKey (User, on_delete=models.PROTECT)
    
    class Meta :
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        
        
    def __str__(self):
        return self.Name
    
    
class Thefac (models.Model):
    """
    name : Thefac model definition 
    Description:
    author : allmoongood2024@gmail.com
    
    """
    
    THEFAC_TYPES =(
        
        ('R','RECU'),
        ('P','FACTURE_INCERTAINE'),
        ('F','FACTURE'),
        
        
    )
    
    client = models.ForeignKey (Client, on_delete=models.PROTECT)
    
    Eng_par = models.ForeignKey (User, on_delete=models.PROTECT)
    
    thefac_date_time = models.DateTimeField(auto_now_add=True)
    
    Total = models.DecimalField (max_digits=100000, decimal_places=4)
    
    Last_updated_date = models.DateTimeField (null=True)
    
    Payer = models.BooleanField (default=False)
    
    Thefac_type = models.CharField (max_length=1, choices=THEFAC_TYPES)
    
    Commentaires = models.TextField (null=True, max_length=2000, blank=True)
    
    
    class Meta :
        verbose_name = "Thefac"
        verbose_name_plural = "Thefacs"
        
    def __str__ (self):
        return f"{self.client.Name}_{self.thefac_date_time}"
    
    
    @property
    def get_total (self):
        articles = self.article_set.all ()
        total = sum (article.get_total for article in articles)
    
    
class Article (models.Model):
    """
    name : Articles model definition
    Description : 
    author :allmoongood2024@gmail.com 
    """
    
    thefac = models.ForeignKey (Client, on_delete=models.CASCADE)
    
    Name = models.CharField (max_length=32)
    
    Quantity = models.IntegerField ()
    
    Prix_unitaire = models.DecimalField (max_digits=1000, decimal_places=2)
    
    Total = models.DecimalField (max_digits=1000, decimal_places=2)
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
        
@property
def get_total (self):
    total = self.quantity * self.prix_unitaire
    