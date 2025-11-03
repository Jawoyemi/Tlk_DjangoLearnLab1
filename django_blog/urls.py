from django.contrib import admin
from django.urls import include, path
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls)),
]
    