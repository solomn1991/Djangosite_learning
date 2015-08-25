# coding:utf-8


from django.conf.urls import url
from . import views

# urlpatterns =[
#    url( r"^$",views.index,name="index"),
#    url( r"^(?P<question_id>[0-9]+)/$",views.detail,name="detail"),
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

urlpatterns = [
    url( r"^index/$",views.index,name="index"),
    url( r"^add/$",views.add,name="add"),
]