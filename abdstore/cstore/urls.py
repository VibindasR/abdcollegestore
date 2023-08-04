from django.urls import path

from cstore import views

app_name = 'cstore'

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]