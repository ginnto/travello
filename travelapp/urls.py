from django.urls import path
from . import views



urlpatterns = [
    path('', views.fun, name='fun')
    # path('func/', views.func, name='func')

    # path('add',views.addtwo,name='add')
]