from django.urls import path
from rango import views

app_name='rango'
urlpatterns =[
    path('',views.index_html_views,name='index_html_views'),
    
    path('about/',views.about_html_views,name='about_html_views'),
    
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    
    path('add_category/', views.add_Category, name='add_category'),
    
    path('category/<slug:category_name_slug>/add_page/', views.add_Page, name='add_page')
    
]