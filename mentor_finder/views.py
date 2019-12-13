from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Mentor
from .forms import CreateMentorForm


def index(request):
    return render(request, 'mentor_finder/index.html')


class CreateMentor(FormView):
    form_class = CreateMentorForm
    template_name = 'mentor_finder/create.html'

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            name = f'{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]}'
            messages.add_message(request, messages.SUCCESS,
                                 f'Successfully added {name}')
            return HttpResponseRedirect(reverse('mentor_finder:create'))

        messages.add_message(request, messages.ERROR,
                             f'An error occurred while attempting to add mentor')
        return render(request, self.template_name, {'form': form})
