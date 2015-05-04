# woot.apps.{{ app_name }}.urls

# django
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('{{ app_name }}.views',
       # (r'^example_url/', 'example_view')
)
