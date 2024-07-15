"""
URL configuration for mokko_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu.views import blog_view, CoffeesView, HomeView, CoffeeView
from django.conf.urls.static import static, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_view, name = 'blog-page'),
    path('coffees/', CoffeesView.as_view(), name = 'coffees-list'),
    path('home/', HomeView.as_view(), name = 'home-list'),
    path('coffee/', CoffeeView.as_view(), name = 'coffee-list')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)