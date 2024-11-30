from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import  LogoutView, LoginView
from django.views.generic import TemplateView, ListView ,DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from .models import UserProfile, Recipe
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm



class LoginPageView(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True

class RegisterPageView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

class LogoutPageView(LogoutView):
    next_page = reverse_lazy('login')


class ProfilePageView(ListView):
    model = UserProfile
    context_object_name = 'profiles'
    template_name = 'app/home.html'



class AboutPageView(TemplateView):
    template_name = 'app/about.html'
    
class ContactPageView(TemplateView):
    template_name = 'app/contact.html'





class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'app/recipe_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'app/recipe_detail.html'


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'description', 'image', 'instructions', 'category']
    template_name = 'app/recipe_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})



class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'image', 'instructions', 'category']
    template_name = 'app/recipe_update.html'

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})



class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'app/recipe_delete.html'
    success_url = reverse_lazy('recipe')