from django.urls import path
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from .views import *

urlpatterns = [
    # path('',index,name='home'),
    path('', HomeView.as_view(), name='home'),
    path('about/', about),
    path('post/<int:pk>', DetailView.as_view(), name='detail_post'),
    # path('post/<int:pk>',DetailView.as_view(),name='detail_post'),
    #  path('add_post/', AddPostClass.as_view(), name='add_post'),
    # path('post/<int:pk>',post_detail, name='detail_post'),
    path('add_post/', AddPost.as_view(),name='add_post'),
    path('add_category/',AddCategory.as_view(),name='add_category'),
    path('cat/<slug:slug>',CategoryView.as_view(),name='category_view'),
    path('register/', RegisterUser.as_view(),name="register"),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('comment/<int:pk>', add_comment,name='add_comment'),
    path('profile/', profile,name='my_profile'),
    # path('my_profile/<int:pk>/', ProfileView.as_view(), name='my_profile'),
    path('like/<int:pk>',like_view,name='like_post'),
    path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    
] 

handler404 = pageNotFound