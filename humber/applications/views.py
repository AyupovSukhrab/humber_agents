from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from applications.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexPageView(TemplateView):
    template_name = 'applications/index.html'

class HomePageView(LoginRequiredMixin, ListView):
    model = Agent
    context_object_name = 'agent_list'
    template_name = 'applications/home.html'

class AgentDetailView(LoginRequiredMixin, DetailView):
    model = Agent
    template_name = 'applications/detail.html'
