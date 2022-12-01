from django.urls import path
from . import views
from .views import searchPageView, resultPageView

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('search/', resultPageView, name='result'),
]
