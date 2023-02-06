from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('register_form_view'))
        return render(request, self.template_name)
