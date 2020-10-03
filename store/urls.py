from django.conf.urls import url
from . import views
from django.http import HttpResponseRedirect
# from django.conf.urls.defaults import *

urlpatterns = [
    url(r'^$', views.store, name='store'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^update_item/$', views.updateItem, name='updateItem'),
    
    
]

# if settings.DEBUG == True:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)