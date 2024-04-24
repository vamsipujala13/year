from django.urls import path

from yearapp import views

urlpatterns = [
    path('',views.home),
    path('year',views.year),
    path('marriage',views.marriage),
]