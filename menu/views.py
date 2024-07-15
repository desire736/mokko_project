from django.views.generic import TemplateView
from .models import Publications, Coffees, Discord, Footer
from django.shortcuts import render

'''
class BlogView(TemplateView):
   template_name = 'blog.html'

   def get_context_data(self, **kwargs):
      context = {
         'blog': Publications.objects.all()
      }
      return context
'''


def blog_view(reguest):
   context = {
      'blog': Publications.objects.all(),
      'footer': Footer.objects.all(),
   }
   respone = render(reguest, 'blog.html', context)
   return respone


class CoffeesView(TemplateView):
   template_name = 'coffees.html'

   def get_context_data(self, **kwargs):
      context = {
         'coffee_list': Coffees.objects.all(),
         'footer': Footer.objects.all(),
      }
      return context


class HomeView(TemplateView):
   template_name = 'index.html'

   def get_context_data(self, **kwargs):


      context = {
         'coffee_list': Coffees.objects.all(),
         'discord_list': Discord.objects.all(),
         'blog': Publications.objects.all(),
         'footer': Footer.objects.all(),
      }
      return context


class CoffeeView(TemplateView):
   template_name = 'coffee.html'

   def get_context_data(self, **kwargs):
      context = {
         'coffee_list': Coffees.objects.all(),
         'footer': Footer.objects.all(),
      }
      return context


