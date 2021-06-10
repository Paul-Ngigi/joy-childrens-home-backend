from django.urls import path
from .views import AllSponsers, SingleSponser

# Apoter urls
urlpatterns = [
    path('', AllSponsers.as_view()),
    path('<int:pk>/', SingleSponser.as_view()),
    path('update/<int:pk>/', SingleSponser.as_view()),
    path('delete/<int:pk>/', SingleSponser.as_view()),
]
