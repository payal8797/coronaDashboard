
from django.contrib import admin
from django.urls import path
from firstPage import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index,name='Mainpage'),
    url('selectCountry',views.drillDownACountry,name='drillDown'),
    url('about',views.about,name='about'),
    url('contactform',views.contactform,name='contactform'),
    url('prec',views.prec,name='prec')
]
