from django.urls import path
from tanselle import views

urlpatterns = [
    path("", views.home, name="home"),
    path('notes', views.notes, name="notes"),
    path('bibnew', views.bibnew, name="bibnew" ),    
    path('bibedit/<int:id>', views.bibedit, name="bibedit" ),    
    path('bibdelete/<int:id>', views.delete_bib, name="delete_bib" ),    
]