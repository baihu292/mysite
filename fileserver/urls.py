from django.urls import path,include,re_path
from django.contrib import admin
from django.views.static import serve
from . import settings
from . import views
urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        path('', include('app.urls')),  # 没有api地址(app)
        path('', include('app.urls')),  # 没有api地址(app)

        path('api/', views.bg_api),       # 获取api
        path('uploadFile01/', views.uploadfile01),   # 有api地址
        path('bh01/', views.wx_data01),    # 有api地址
        re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})

]