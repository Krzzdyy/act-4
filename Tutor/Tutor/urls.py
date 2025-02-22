from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/', include('student_info.urls')),
    path('', include('student_info.urls')), 
]