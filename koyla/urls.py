from django.conf.urls import url, include
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'koyla', views.KoylaSet)

urlpatterns = [
#    url(r'^/(?P<word>.+)/$', include(router.urls))
	    url(r'^(?P<word>.+)/$', views.KoylaSet.as_view())
]