from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url('^home1.html',views.index1,name = 'home1'),
    url('^home2.html',views.index2,name = 'home2'),
    url(r'^search/',views.search_by_category, name='search_by_category'),
    url(r'^location/(?P<location>\d+)', views.search_by_location, name='location_filter'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)