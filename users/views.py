from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignUpForm


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('posts:_post')

    # def form_valid(self, form):
    #     form.save()
    #     email = form.cleaned_data.get('email')
    #     password = form.cleaned_data.get('password')
    #     user = authenticate(self.request, username=email, password=password)
    #     if user is not None:
    #         login(self.request, user)
    #     user.verify_email()
    #     return super().form_valid(form)
