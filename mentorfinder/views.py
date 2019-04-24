from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CreateForm

def index(request):
    return render(request, 'mentorfinder/index.html')

class CreateView(View):
    form_class = CreateForm
    template_name = 'mentorfinder/create.html'

    def get(self, request):
        return render(request, 'mentorfinder/create.html')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/create/')
        return render(request, self.template_name, {'form': form})
