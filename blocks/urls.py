from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^block/',views.show_index,name='specific blocks'),
    url(r'^userprofile/',views.show_index,name='user profile'),
    url(r'^book',views.show_index,name='books'),
    url(r'^books/', RedirectView.as_view(pattern_name='bulb:index')),
    url(r'^newbook',views.show_index,name='add a new book')
]
