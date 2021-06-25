import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('test_app.urls', namespace='test_app'))

]
