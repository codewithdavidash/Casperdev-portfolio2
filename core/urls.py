from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('projects/', project, name='project'),
    path('services/', services, name='services'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('blog/', blog, name="blog"),
]
