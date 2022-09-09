from django.contrib import admin
from django.urls import path, include
from blog.views import PostViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", PostViewset, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('posts/', include(router.urls)), 
    path('auth/', include('accounts.urls')),
]
