from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_app import views
from rest_framework.authtoken import views as drf_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'reviews', views.ReviewViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', drf_views.obtain_auth_token)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
