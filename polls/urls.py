from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pergunta/<int:pk>/', QuestionView.as_view(), name='pergunta'),
    path('pergunta/<int:pk>/resultados/', ResultsView.as_view(), name='resultados'),
]
