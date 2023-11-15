from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('new', views.add_show, name= 'new_show'),
    
    path('<int:show_id>', views.display, name= 'display'),
    path('<int:show_id>/edit', views.update, name= 'edit'),
    path('<int:show_id>/delete', views.delete, name= 'delete'),

    path('create', views.add_show),
] 