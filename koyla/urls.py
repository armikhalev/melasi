from django.conf.urls import url
from . import views

urlpatterns = [
	    url('^english/(?P<word>.+)/$', views.EngSet.as_view()),
	    url('^mela/(?P<la>.+)/$', views.MelaSet.as_view()),
]
