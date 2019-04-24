from django.forms import ModelForm

from .models import Mentor

class CreateForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'phone', 'available']
