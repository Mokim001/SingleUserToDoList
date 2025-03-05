#mokim jobs is to create urls and views on app
from django.urls import path
from app.views import *
urlpatterns = [
    path("",home,name='home'),
    path("update<pk>",update,name='update'),
    path("delete<pk>",delete,name='delete'),
]
