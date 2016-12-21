from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from app import views

urlpatterns = [
    url(r'^api/v1/feedbacks$', views.get_feedbacks, name='get_feedbacks'),
    url(r'^api/v1/feedbacks/post$', views.post_feedback, name='post_feedback'),
    url(r'^api/v1/events$',  views.get_events, name='get_events'),
    url(r'^api/v1/chapters$',  views.get_chapters, name='get_chapters'),
    url(r'^api/v1/districts$',  views.get_districts, name='get_districts'),
    url(r'^api/v1/ministrys$',  views.get_ministrys, name='get_ministrys'),
    url(r'^api/v1/ministrys/(?P<pk>[0-9]+)$', views.get_ministry, name='get_ministry'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
