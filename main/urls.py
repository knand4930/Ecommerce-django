from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views 

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^contact/$', views.contact_page, name='contact_page'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^register/$', views.register_page, name='register_page'),
]


