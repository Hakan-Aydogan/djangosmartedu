
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(
            available=True).order_by('-date')[:2]
        context['course_count'] = Course.objects.filter(available=True).count()
        context['students_count'] = User.objects.filter(is_active=True).count()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactFormView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We got your message. We will back to you soon. '

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
