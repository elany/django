from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
)

def post_detail(request, pk):
	Post.objects.get_object_or_404(pk=pk)