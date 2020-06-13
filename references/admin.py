from django.contrib import admin
from .models import References

@admin.register(References)
class ReferencesAdmin(admin.ModelAdmin):
    list_display = ('titleRf', 'descriptionRf', 'linkRf','authorRf','statusRf','createdRf')
    list_filter = ('titleRf', 'descriptionRf', 'linkRf','authorRf','statusRf','createdRf')
    search_fields = ('titleRf', 'descriptionRf')
    raw_id_fields = ('authorRf',)
    
  
  

