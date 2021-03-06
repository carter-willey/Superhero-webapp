from . import views
from django.urls import path
app_name = 'heroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_hero'),
    path('<int:specific_hero_id>/edit/', views.edit, name='edit'),
    path('<int:specific_hero_id>/delete/', views.delete, name='delete'),
]