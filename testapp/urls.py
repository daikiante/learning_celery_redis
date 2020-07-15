from django.urls import path

from . import views

app_name = 'testapp'
urlpatterns = [
    path('celery_test/', views.celery_test, name='celery_test'),
]
