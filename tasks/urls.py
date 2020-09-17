from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('deleteAll/', views.deleteAll, name='deleteAll'),
    path('update_page/<int:task_id>', views.update_page, name='update_page'),
    path('update/<int:task_id>', views.update, name='update')
]
