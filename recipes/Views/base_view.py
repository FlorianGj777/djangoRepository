from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'

    def user(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return None
        return self.request.user.get_username()
