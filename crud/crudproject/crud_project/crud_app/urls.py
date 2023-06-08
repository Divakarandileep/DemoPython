from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),

    # path('details',views.details,name='details')

]