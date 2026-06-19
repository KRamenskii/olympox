from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserLoginForm

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True
    extra_context = {
        'show_header': False,
    }


class UserLogoutView(LogoutView):
    next_page = 'login'