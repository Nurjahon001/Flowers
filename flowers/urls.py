from django.urls import path
from .views import FlowerList,FlowerDetailView

app_name = 'flowers'
urlpatterns=[
    path('',FlowerList.as_view(), name='flower-list'),
    path('<int:pk>/flower-detail/',FlowerDetailView.as_view(), name='flower-detail'),

]