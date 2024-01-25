from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View


# Create your views here.
class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  )


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'register.html'


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from store.models import Customer
from .forms import ProfileForm


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(user=request.user)
        return render(request, self.template_name, {'user_profile': user_profile})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'edit_profile.html'

    def get(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=user_profile)
        return render(request, self.template_name, {'form': form, 'user_profile': user_profile})

    def post(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form, 'user_profile': user_profile})


class CreateProfileView(View):
    template_name = "create_profile.html"

    def get(self, request, *args, **kwargs):
        print("user:", request.user)
        user_profile = Customer.objects.create()
        form = ProfileForm(instance=user_profile)
        return render(request, self.template_name, {'form': form, 'user_profile': user_profile})

    def post(self, request, *args, **kwargs):
        user_profile = Customer.objects.get()
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form, 'user_profile': user_profile})
