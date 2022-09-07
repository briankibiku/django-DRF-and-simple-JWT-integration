from unicodedata import name
from django.urls import path, include
from . import views
from blog.views import PostViewset, PostViewsetModal
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", PostViewsetModal, basename="posts")


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('homepage', views.homepage, name='posts_home'),
    path('posts/', include(router.urls)),
    path('', views.PostListCreateMixinView.as_view(), name='list_posts'),
    path('homepagedjango', views.homepagedjango, name='posts_homedjango'),
    path('<int:pk>', views.PostRetrieveUpdateDeleteView.as_view(), name='post_detail'),
]
