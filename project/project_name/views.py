from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from blog.models import Article
from django.core.mail import send_mail
from {{project_name}}.forms import ContactForm

class HomePageView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['top4articles'] = Article.objects.filter(is_active=True)[:4]
        return context

class ContactPageView( FormView ):
    template_name="contact.html"
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        recipients = ('CHANGE_ME@{{ project_name }}.com',)
 
        send_mail(subject, message, sender, recipients)
        return super(ContactPageView, self).form_valid(self)
        
class RobotPageView(TemplateView):
    template_name="robots.txt"
    content_type='text/plain'
    
class HumanPageView(TemplateView):
    template_name="humans.txt"
    content_type='text/plain'

#class GooglePageView(TemplateView):
#    template_name="googleXXXXXXXXXXX.html"
#    content_type='text/plain'
