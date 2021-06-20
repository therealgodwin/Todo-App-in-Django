from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name="register"),
    path('register_user', views.register_user, name="register_user"),
    path('login', views.login_page, name="login"),
    path('login_user', views.login_user, name="login_user"),
    path('logout', views.logout_user, name="logout"),
    path('home', views.home, name="home"),
    path('add_task', views.add_task, name="task_add"), 
    path('delete_task/<int:pk>', views.delete_task, name="task_delete")
]
