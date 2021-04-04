from django.urls import path
from .views import save_stopwords_to_model

app_name = 'topick_defined'

urlpatterns = [
    path('', save_stopwords_to_model, name='save_stopwords'),
]