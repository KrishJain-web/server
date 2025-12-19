"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from home.views import home,about,services,askagain
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_with_openai, name='chat_with_openai'),





    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('askagain', askagain, name='askagain'),
    # path('ask_llm/', ask_llm, name='ask_llm'),
]
