from django.views.generic import FormView, TemplateView

from .forms import NewsLetterModelForm


class NewsLetterModelView(FormView):
    template_name = 'newsletters/email_form.html'
    form_class = NewsLetterModelForm
    success_url = '/newsletters/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'newsletters/success.html'
