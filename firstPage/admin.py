from django.contrib import admin    
from .models import form
# Register your models here.
@admin.register(form)

class formAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','country','subject']