from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('gold', views.default_view),
    path('post', views.handle_post),
    path('', views.times_table),
    path('pacman', views.pacman)
]

urlpatterns += staticfiles_urlpatterns()