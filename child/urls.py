from django.urls import path
from .views import AllChildren, SingleChild

# Child urls
urlpatterns = [
    path('', AllChildren.as_view()),
    path('<int:pk>/', SingleChild.as_view()),
    path('update/<int:pk>/', SingleChild.as_view()),
    path('delete/<int:pk>/', SingleChild.as_view()),
]
