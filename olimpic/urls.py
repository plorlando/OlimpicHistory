from django.urls import path
from .views import *
from . import views

app_name = 'olimpic'

urlpatterns = [
    path('', home, name='home'),
    path('noc_list/', views.NOCList.as_view(), name='noc_list'),
    path('noc_update/<str:pk>', views.NOCUpdate, name='noc_update'),
    path('noc_new', views.NocNewView.as_view(), name='noc_new'),
    path('noc_delete_confirm/<str:pk>', views.NocDeleteView.as_view(), name='noc_delete'),
    path('athlete_events/', AthleteList.as_view(), name='athlete_list'),
    path('athlete_update/<int:pk>', views.AthleteUpdate, name='athlete_update'),
    path('athlete_new', views.AthleteNewView.as_view(), name='athlete_new'),
    path('athlete_delete_confirm/<int:pk>', views.AthleteDeleteView.as_view(), name='athlete_delete'),

]