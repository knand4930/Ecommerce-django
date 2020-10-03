from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views 
import random
import string



urlpatterns = [
    url(r'^product/$', views.product_list_view, name='product_list_view'),
    url(r'^products/$', views.ProductListView.as_view(), name='products'),
    url(r'^product/(?P<pk>\d+)$', views.product_detail_view, name='product_detail_view'),
    # url(r'^products/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', views.ProductSlugDetailView.as_view(), name='products'),
    url(r'^features/$', views.ProductFeaturedListView.as_view(), name='feature'),
    url(r'^features/(?P<pk>\d+)/$', views.ProductFeaturedDetailView.as_view(), name='feature'),

] 