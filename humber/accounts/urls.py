from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
]