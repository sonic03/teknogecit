from django.contrib import admin
from django.urls import path
from . import views

app_name="articles"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name="addarticle"),
    path('article/<slug:slug>',views.details,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('comment/<int:id>',views.addcomment,name="comment"),
    path('visit/<int:id>',views.visitor,name="visitor"),
    path('likes/<int:id>',views.likes,name="likes"),
    path('addCategory/',views.addCategory,name="addCategory"),
    path('test-session/', views.test_session, name='test_session'),
    path('members/', views.members, name='members'),
    
    
   

]