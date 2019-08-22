from django.urls import path
from django.views.static import serve
from . import views
urlpatterns = [
        path('uploadFile/', views.uploadfile),
        path('bh/', views.wx_data)
]