from django.contrib.auth.models import User
from django.core.checks import messages
from django.urls import reverse
from django.views import generic

from recipes.forms.register import RegisterForm


class RegisterFormView(generic.FormView):
    template_name = 'resgister_form.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['user_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            User.objects.create_user(
                username=username, email=email, password=password
            )
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
