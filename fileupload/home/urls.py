from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path('download/<uid>' , views.download),
    path('handle/', views.HandleFileUpload.as_view())

]