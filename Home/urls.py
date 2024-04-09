from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index,name='index'),
    path ('about/',views.about,name='about'),
    path ('customer/',views.customer,name='customer'),
    path ('add/',views.add_customer,name='add'),
    path ('update/<int:id>/',views.update_customer,name='update'),
    path ('delete/<int:id>/',views.delete_customer,name='delete'),
    
    path ('additem/',views.add_item,name='additem'),
    path ('updateitem/<int:id>/',views.update_item,name='updateitem'),
    path ('deleteitem/<int:id>/',views.delete_item,name='deleteitem'),
    path ('info/<int:id>/',views.retrive_item, name ='info'),
    
    
    path ('check/',views.check,name='check'),
    
    path ('user/',views.user,name='user'),
]
