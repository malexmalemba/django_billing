from django.contrib import admin
from .models import *

# Register your models here.


class AdminClient(admin.ModelAdmin):
    list_display = ('Name', 'Email','Telephone','Adresse','Sexe','Age','Ville','Code_postal','Date','Eng_par')

    
class AdminThefac(admin.ModelAdmin):
    list_display = ('client','Eng_par','Total','client_date_time','Last_updated_date','Payer','Thefac_type','Commentaires')
    

admin.site.register (Client,AdminClient)
admin.site.register (Thefac,AdminThefac)
admin.site.register (Article)

