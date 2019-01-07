from django.urls import path
from .views import OfferingListView, OfferingDetailView, OfferingCreateView, OfferingUpdateView, OfferingDeleteView
from . import views

urlpatterns = [
    path('', OfferingListView.as_view(), name='curriculum-home'),
    path('offering/<int:pk>/', OfferingDetailView.as_view(), name='offering-detail'),
    path('offering/<int:pk>/update/', OfferingUpdateView.as_view(), name='offering-update'),
    path('offering/<int:pk>/delete/', OfferingDeleteView.as_view(), name='offering-delete'),
    path('offering/new/', OfferingCreateView.as_view(), name='offering-create'),
    path('about/', views.about, name='curriculum-about'),
]