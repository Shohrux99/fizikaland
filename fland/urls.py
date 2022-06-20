from django.urls import path,include
from .views import IndexView,first,second,third,fourth,fifth
urlpatterns = [
    path('',IndexView,name='index'),
    path('first/', first,name='first'),
    path('second/', second,name='second'),
    path('third/', third,name='third'),
    path('fourth/', fourth,name='fourth'),
    path('fifth/', fifth,name='fifth'),
]
