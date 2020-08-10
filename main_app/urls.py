from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('gold/', include('ninja_gold_app.urls')),
    path('pacman/', include('pacman_app.urls')),
    path('timestable/', include('timestable_app.urls')),
]