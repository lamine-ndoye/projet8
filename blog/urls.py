
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<slug:category>/', views.post_list, name='category_post_list'),
    path('<int:year>/<int:month>/<int:day>/<details>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<detail>/update/', views.post_update, name='post_update'),
    path('search/' , views.post_search, name='post_search'),
    path('form/' , views.add_post,  name='add_post'),
]
