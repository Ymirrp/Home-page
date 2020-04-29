from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home_app import views
from user_config_app import views as user_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('weather/', views.get_weather_view, name='weather'),
    path('out/<path:url>', views.reroute, name='topsites-url'),
    path('add-site/', views.add_site, name='add-site'),
    path('edit/<int:s_id>', views.edit_site, name='edit-site'),
    path('del/<int:s_id>', views.del_site, name='del-site'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register/', views.user_reg, name='register'),
    # path('profile/', views.unavailable, name='profile-site'),
    path('profile/', user_views.index, name='profile'),
    path('profile/change-password/',
         auth_views.PasswordChangeView.as_view(template_name='pw_change.html'), name='password_change'),
    path('profile/change-password/done',
         auth_views.PasswordChangeDoneView.as_view(template_name='pw_change_done.html'), name='password_change_done'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('profile/reset/', user_views.reset, name='pw-reset'),
    path('todo/', views.unavailable, name='todo-site'),
    path('calendar/', views.unavailable, name='calendar-site'),
    path('admin/', admin.site.urls),
]
