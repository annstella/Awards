from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/projects$', views.new_projects, name='new-projects'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^api-token-auth/', obtain_auth_token)
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)