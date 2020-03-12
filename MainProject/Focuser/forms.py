from django.forms import ModelForm
from .models import Eclipse, Favorite

#Create the form class.
class EclipseForm(ModelForm):
    class Meta:
        model = Eclipse
        fields = '__all__'

class FavoriteForm(ModelForm):
    class Meta:
        model = Favorite
        fields = '__all__'
