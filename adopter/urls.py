from django.urls import path
from .views import AllAdopters, SingleAdopter

# Child urls
urlpatterns = [
    path('', AllAdopters.as_view()),
    path('<int:pk>/', SingleAdopter.as_view()),
    path('update/<int:pk>/', SingleAdopter.as_view()),
    path('delete/<int:pk>/', SingleAdopter.as_view()),
]
