from django.forms import ModelForm
from .models import Plant

#Create the form class.
class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'