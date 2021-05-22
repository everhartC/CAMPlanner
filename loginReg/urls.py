from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('myAccount/<int:id>', views.profile, name="myProfile"),
    path('myAccount/<int:id>/myGear', views.myGear, name="myGear"),
]