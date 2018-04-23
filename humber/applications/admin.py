from django.contrib import admin
from applications.models import Agent, AgentStatus

admin.site.register(Agent)
admin.site.register(AgentStatus)