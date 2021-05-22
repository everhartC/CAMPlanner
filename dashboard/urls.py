from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('addTrip', views.addTrip, name='addTrip'),
    path('trip/<int:tripid>', views.viewTrip, name="viewtrip"),
    path('trip/<int:tripid>/edit', views.editTrip, name="editTrip"),
]