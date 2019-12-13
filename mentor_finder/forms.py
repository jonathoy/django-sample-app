from django.forms import ModelForm

from .models import Mentor


class CreateMentorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateMentorForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['available'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Mentor
        fields = ['email', 'first_name', 'last_name', 'phone', 'available',]
