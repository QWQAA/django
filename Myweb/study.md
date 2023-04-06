# Django 学习记录
**一、配置django环境**    
专业版直接新建django项目就行，社区版需要先安装django安装包通过命令生成django项目之后再通过pycharm继续进行配置     
项目创建命令： 

`django-admin startproject projecename` 
    
通过上面的命令就可以创建一个django项目  
注意的几个点：     
1、需要在创建项目的目录下创建项目；  
2、需要提前将django配置到系统环境中，否则会查无指令；  、
3、建议通过pip或者pycharm安装django库，会自动添加环境变量；  
4、手动配置环境变量是将
Python 目录下的Lib\site-packages\django和Scripts加入到系统变量的 Path 中

**二、创建项目成功首次启动**    
在控制台输入:
`python manage.py runserver`
即可启动服务，通过访问网址出现示例图片
[首次出现网址](https://img-blog.csdnimg.cn/20200208205605462.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NjZm9yMzMz,size_16,color_FFFFFF,t_70)
    
**三、创建数据库**     
一般情况下数据库都是网站的核心，没有数据库的支撑，网站的数据无法实现交互。   
django默认是使用sqlite3，需要修改为自己的mysql数据库，需要通过以下操作：   
1、首先新建一个数据库，完成数据库的测试链接：     
推荐下载DB Navigator可以在pycharm中使用数据库操作。     
2、 修改配置文件：
打开 '_init_.py'文件添加支持

`import pymysql`

`pymysql.install_as_MySQLdb()  # django链接mysql初始化`  
3、修改setting.py文件    
`DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',  # 数据库类型
'NAME': 'myweb',  # 所使用的数据库的名字
'USER': 'root',   # MySQL user
'PASSWORD': '123456',
'HOST': '127.0.0.1',  # 数据库地址
'PORT': '3306',   # 端口
}
}`
    
4、完成配置数据的表单的迁移  
代码：
`pytohn manage.py migrate`
    
**四、创建超级管理员账户** 
代码：
`python manage.py createsuperuser`  
输入账户：whh    
密码：123456   

**五、创建个人web**   
代码：
`python manage.py startapp appname` 

通过上述代码可以生成个人的系统网站模板，接下来需要配置个人应用.    
1、配置应用： 
主项目文件 urls.py （路由文件配置）：     
添加个人路由位置，在个人web配置文件里添加路由文件urls.py   
在主文件里将个人添加的路由位置导入
用到include包
`path('whhs/', include("whhs.urls")), # 添加个人的路径`
    
配置个人项目下的urls文件，配置应用子路由： 

`urlpatterns={
path('', views.toLogin_view, name= 'login')  # 路径控制
}`  
用于访问界面的路径跳转     
2、views(渲染界面)   
配置个人的渲染界面
`return render(request, 'login.html')   # 返回界面` 
    
3、创建模板和html：     
（1）、配置setting。py(TEMPLATES0)配置项 

`TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [os.path.join(BASE_DIR, 'filename（自己创建）')],}]  # 配置路径(完成路径的拼接)
`   
添加app路径到setting.py配置文件  
`INSTALLED_APPS = [
'whh']
`

（2）、创建前端网页（html）：    
新建HTML项目文件（filename）    
创建前端网页  
**现在你已经得到一个属于你的网页了**

**六、简单逻辑处理**    
网页安全机构：
`{%csrf_token%} `   
剩下的类似于Java的web处理方式  
需要注意写完逻辑处理方法之后需要添加的路径到路由中，  
**七、数据库做登陆操作**  
1、在model.py中创建数据模型，需要用到models库  
简单一个例子: 

`class StudentInfo(models.Model):
stu_id = models.UUIDField(primary_key=True, max_length=10)
stu_user = models.CharField(max_length=20, null=False)
stu_pwd = models.CharField(max_length=20, null=False)`  
2、将数据模型迁移至数据库   
`python manage.py makemigrations 用户名`   
用于生成migrations数据库迁移文件文件 

`python manage.py migrate`  
在数据库中生成table    
3、确保数据库中存有数据    
4、通过models.py,将前端获取的数据同数据库的比对
