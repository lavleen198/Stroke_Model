from django.urls import path
from classification import views
app_name='classification'
urlpatterns=[
    path('',views.index,name='form_log'),
    path('result',views.result,name='result'),
]
