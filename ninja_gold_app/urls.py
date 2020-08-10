from django.urls import path, include
from . import views

urlpatterns = [
    path('post', views.handle_post),
    path('', views.default_view),
]