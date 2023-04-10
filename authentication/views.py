from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.template import RequestContext

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'authentication/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['email'] = self.request.user.email
        return context
