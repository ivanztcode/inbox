
from django.contrib import admin
from django.urls import path, include
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name="home"),
    path("inbox",views.inbox,name="inbox"),
    # path para el login y el logout
    path("login/",include("django.contrib.auth.urls"))
]
