from django.urls import path
from pochinki import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.BlogPage, name='home'),
    path('add/', views.add_player, name='add'),
    path('edit/<int:id>/', views.edit_player, name='edit'),
    path('delete/<int:id>/', views.delete_player, name='delete'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.use_register, name='register'),
    
    path('registrationpage', views.akatsuki, name='regform'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
