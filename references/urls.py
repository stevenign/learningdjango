from django.urls import path
from . import views

app_name='references'
urlpatterns = [
    path('', views.references_list, name='references_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:references>/', views.references_detail, name='references_detail'),
    path('references/add/', views.ReferencesCreateView.as_view(), name='references_create'),
    path('references/<int:pk>/update/', views.ReferencesUpdateView.as_view(), name='references_update'),
    path('references/<int:pk>/delete/', views.ReferencesDeleteView.as_view(), name='references_delete'),
]
