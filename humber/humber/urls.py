from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    url('admin/', admin.site.urls),
    url('^', include('applications.urls', namespace = 'applications')),
    url('^accounts/', include('accounts.urls', namespace='accounts')),
]