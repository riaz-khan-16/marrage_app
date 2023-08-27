from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from public import views

urlpatterns = [
    path('persons/', views.intro_list),
    path('person/<int:pk>/', views.intro_detail),
    path('regi/', views.regi),
    path('dregi/', views.detail_regi),
    path('', views.dashboard),
    path('public/', views.public,name='public'),
    path('login/', views.login1, name='login1'),
    path('logout/', views.logout1, name='logout1'),
    path('successfull/', views.success, name='success'),


]

urlpatterns = format_suffix_patterns(urlpatterns)