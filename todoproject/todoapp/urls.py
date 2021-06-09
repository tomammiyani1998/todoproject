from . import views
from django.urls import path
app_name = 'todoapp'


urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('homelistview/', views.Tasklistview.as_view(), name='homelistview'),
    path('detailview/<int:pk>/', views.Taskdetailview.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.Taskupdateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.Taskdeleteview.as_view(), name='deleteview'),
]