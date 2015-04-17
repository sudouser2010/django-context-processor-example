from django.conf.urls import patterns, include, url
from django.contrib import admin
import demosite.views

urlpatterns = patterns('',
    url(r'^about$',     demosite.views.about),
    url(r'^contact$',   demosite.views.contact),
    url(r'^',           demosite.views.home),
)
