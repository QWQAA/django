from django.urls import path
from . import views  # 渲染界面

# app_name = 'whhs'
# 添加路径
urlpatterns = [
    path('', views.toLogin_view, name='login'),   # 路径控制
    path('index/', views.toIndex_view, name='index'),


]