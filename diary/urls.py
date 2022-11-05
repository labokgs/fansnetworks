from django.urls import path

from . import views
from diary.views import top

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('top/', top, name='top'),
]
