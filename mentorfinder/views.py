from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Mentor
from .forms import CreateMentorForm


def index(request):
    return render(request, 'mentorfinder/index.html')

class CreateMentor(FormView):
    form_class = CreateMentorForm
    template_name = 'mentorfinder/create.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            mentor = Mentor.objects.create(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                available=form.cleaned_data['available'],
            )
            messages.add_message(
                request, messages.SUCCESS, f'Successfully added {mentor.first_name} {mentor.last_name}!'
            )
            return HttpResponseRedirect(reverse('create'))
        messages.add_message(
            request, messages.ERROR, f'An error occurred while attempting to add {mentor.first_name} {mentor.last_name}'
        )
        return render(request, self.template_name, {'form': form})
