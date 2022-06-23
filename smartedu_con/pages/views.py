
from django.views.generic import TemplateView
from courses.models import Course

# Create your views here.

class IndexView(TemplateView):
    template_name= "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['course_count'] = Course.objects.filter(available=True).count()
        return context

class AboutView(TemplateView):
    template_name= 'about.html'


