from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^api/post_data/(?P<bio>[\w\-]+)/(?P<name>[\w\-]+)/(?P<phone_number>[\w\-]+)$', views.postData, name="post"),
    url(r'^api/profile_list/$', views.ProfileList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)