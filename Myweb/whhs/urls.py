from django.urls import path
from . import views  # 渲染界面

# app_name = 'whhs'
# 添加路径
urlpatterns = [
    # 路径控制
    path('101/', views.to_register, name='register'),    # 注册界面
    path('register/', views.register_view),          # 注册逻辑处理地址
    path('102/', views.toLogin_view, name='login'),      # 登录界面
    path('index/', views.toIndex_view, name='index'),  # 登录逻辑处理

]