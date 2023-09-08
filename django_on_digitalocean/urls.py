from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import authentication.views
import topblog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", topblog.views.home, name="home"),
    path("home/", topblog.views.home, name="home"),
    path('login/', LoginView.as_view(
        template_name="authentication/login.html",
        redirect_authenticated_user=True
    ), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("signin/", authentication.views.signin, name="signin"),
]
