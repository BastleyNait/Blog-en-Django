from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detalle/<str:title>', views.detalle, name='detalle'),
    path('crear/', views.new, name='new' )
]
