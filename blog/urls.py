from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detalle/<int:pk>', views.detalle, name='detalle'),
    path('crear/', views.new, name='new' )
]
