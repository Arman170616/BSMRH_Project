from django.urls import path

from .views import main_view
app_name = 'appthree'

urlpatterns = [
    path('', main_view, name = 'main-view'),
]
