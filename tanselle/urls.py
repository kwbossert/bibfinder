from django.urls import path
from tanselle import views

urlpatterns = [
    path("", views.home, name="home"),
    path('bibnew', views.bibnew, name="bibnew" ),    
    path('bibedit/<int:id>', views.bibedit, name="bibedit" ),    
    path('delete_bib/<int:id>', views.delete_bib, name="delete_bib" ),    
]