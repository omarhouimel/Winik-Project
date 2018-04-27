from django.contrib import admin

# Register your models here.
from home.forms import SingupForm
from home.models import GaleriePhoto, Contact, Position

admin.site.register(GaleriePhoto)
admin.site.register(Contact)
admin.site.register(Position)