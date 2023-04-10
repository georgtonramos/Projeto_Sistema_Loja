from django.urls import path, re_path
from .views import CustomLoginView, RegisterView, DashboardView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.template import RequestContext
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]