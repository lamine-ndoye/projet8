from django.urls import path


from .import views

urlpatterns = [
    path('login/', views.Login_view, name='login_view'),
    path('logout/', views.Logout_view, name='logout_view'),
    path('register/', views.Register_view, name='register_view'),
]
