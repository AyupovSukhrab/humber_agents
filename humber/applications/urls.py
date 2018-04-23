from django.conf.urls import url
from applications.views import IndexPageView, HomePageView, AgentDetailView

app_name = 'applications'

urlpatterns = [
    url(r'^$', IndexPageView.as_view(), name='index'),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', AgentDetailView.as_view(), name='detail'),
]