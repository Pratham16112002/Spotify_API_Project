
from django.urls import path
from .views import index 

app_name = 'frontend'

urlpatterns = [
    path('',index,name=''),
    path('join',index),
    path('create',index),
    path('room/<str:roomCode>',index)
    # the above str means that it will accept any string after room/{any string} , two provide any interger we need to specify it as <int:{}>
]

