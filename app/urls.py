from django.conf.urls.defaults import *
#from django.conf import settings

#from .models import 

urlpatterns = patterns('app.views',
    url(r'^$', 'home', name='home'), #default url
)

#urlpatterns += patterns('',
#    url(r'^example/$', 'django.views.generic.simple.redirect_to', 
#                        {'url': '/', 'permanent': False}),
#)
