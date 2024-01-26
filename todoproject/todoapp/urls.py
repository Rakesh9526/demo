from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepg,name='homepage'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:upid>/',views.update,name='update'),
    path('cbview/',views.tlistview.as_view(),name='cbview'),
    path('dtview/<int:pk>/',views.detailview.as_view(),name='dtview'),
    path('upview/<int:pk>/',views.updateview.as_view(),name='upview'),
    path('dlview/<int:pk>/',views.deleteview.as_view(),name='dlview'),
]