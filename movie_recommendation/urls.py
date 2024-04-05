from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from recommender import views

urlpatterns = [
    path('', include('recommender.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)