from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import resolve_url

signup = CreateView.as_view(
    form_class = UserCreationForm,
    #기본 URL을 변경
    template_name = 'accounts/form.html',
    #로그인 성공했을 때 보낼 URL
    success_url = settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
    next_page = 'blog_main'
)

class CustomLogoutView(LogoutView):
    @property
    def next_page(self):
        if 'next' in self.request.GET:
            return self.request.GET['next']
        else:
            return resolve_url(settings.LOGIN_URL)

logout = CustomLogoutView.as_view()

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')