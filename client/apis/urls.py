from django.urls import path
from .views import create, get


urlpatterns = [
    path('get/',get.GetDocsForClient),
    path('get/<str:doc_id>/',get.GetDoctor),
    path('create/<str:doc_id>/',create.CreateClient),

]