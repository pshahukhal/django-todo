from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('delete/<id>', views.delete, name='delete'),
	path('mark_on/<id>', views.mark_on, name='mark_on'),
	path('mark_off/<id>', views.mark_off, name='mark_off'),
	path('edit/<id>', views.edit, name='edit'),
    path('filter/<status>',views.filter,name='filter'),
    path('mark_all_on',views.mark_all_on,name="mark_all_on"),
    path('mark_all_off',views.mark_all_off,name="mark_all_off")
	
]