from django.urls import path
from django.contrib import admin

from myapp.views import ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDeleteView.as_view(), name='project-list-create'),
]
