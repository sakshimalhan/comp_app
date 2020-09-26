from django.urls import path
from api import views
urlpatterns=[
    path('',views.Home.as_view()),
    path('<int:pk>',views.Details.as_view()),


]