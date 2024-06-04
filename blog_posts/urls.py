from django.urls import path
from . import views
urlpatterns = [
    path("",views.index.as_view(),name="index"),
    path("all_posts",views.all_posts.as_view(),name="all_posts"),
    path('all_posts/<slug:slug>', views.one_post.as_view(),name="post"),
    path('all_posts/<slug:slug>/read_later',views.addReadLater.as_view(),name="set_read_later"),
    path("read_later",views.readLater.as_view(),name="read_later"),
    path('create_post',views.createPost.as_view(),name = "create_view"),
    path("register", views.registerUser.as_view(),name="register"),
    path('login',views.loginUser.as_view(),name="login"),
    path('profiles/<str:name>',views.profile.as_view(),name='profile'),
    path('log_out',views.logOut.as_view(),name='logout')
]
