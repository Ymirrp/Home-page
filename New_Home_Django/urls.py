from django.contrib import admin
from django.urls import path, include
from home_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('out/<path:url>', views.reroute, name='topsites-url'),
    path('add-site/', views.add_site, name='add-site'),
    path('edit/<int:s_id>', views.edit_site, name='edit-site'),
    path('del/<int:s_id>', views.del_site, name='del-site'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register/', views.user_reg, name='register'),
    path('profile/', views.unavailable, name='profile-site'),
    # path('profile/', include('home_app.urls'), name='profile-urls'),
    path('todo/', views.unavailable, name='todo-site'),
    path('admin/', admin.site.urls),
]
