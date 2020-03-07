from django.forms import ModelForm
from .models import Eclipse

#Create the form class.
class EclipseForm(ModelForm):
    class Meta:
        model = Eclipse
        fields = '__all__'
