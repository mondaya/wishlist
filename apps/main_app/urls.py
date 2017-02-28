from django.conf.urls import url
import views

urlpatterns = [ 
    url(r'^$', views.index, name='home'),
    url(r'^create$', views.create, name='create'),
    url(r'^add$', views.add, name='add'),
    url(r'^(?P<item_id>\d+)$', views.show, name='show'),
    url(r'^(?P<item_id>\d+)/add$', views.addTo, name='addTo'),
    url(r'^(?P<item_id>\d+)/delete$', views.delete, name='delete'),
    url(r'^(?P<item_id>\d+)/remove$', views.remove, name='remove'),
    
]