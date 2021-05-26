from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('addTrip', views.addTrip, name='addTrip'),
    path('trip/<int:tripid>', views.viewTrip, name="viewtrip"),
    path('trip/<int:tripid>/edit', views.editTrip, name="editTrip"),
    path('trip/<int:tripid>/addMsg', views.addMsg, name="addMsg"),
    path('user/<int:uid>/deleteMsg/<int:msgid>', views.deleteMsg, name='deleteMsg'),
]