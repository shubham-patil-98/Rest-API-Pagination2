from django.contrib import admin
from django.urls import path
from pageapp import views

urlpatterns = [
    path('studentapi',views.StudentList.as_view()),
    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
]