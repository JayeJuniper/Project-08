from django.urls import path

from minerals import views


urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('search/', views.search, name='search'),
    path('<str:letter>/', views.mineral_by_letter, name='letterlist'),
    path('Group/<str:group>/', views.mineral_by_group, name='group'),
    path('More/<str:group>/', views.mineral_more, name='more'),
    path('Special_Search/<str:special>:<str:group>/', views.special_search, name='special'),
    path('Mineral/<int:pk>/', views.mineral_detail, name='detail'),
]