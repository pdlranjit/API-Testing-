
from django.urls import path
from . import views

urlpatterns = [
    
    path('details/',views.Details,name='details'),
    path('details/<int:id>',views.Details_list,name='new_details')
]
