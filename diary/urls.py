from django.urls import path
from django.contrib import admin
from .models import Diary
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from . import views

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ('name', 'address', 'lat', 'lng')

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = PlaceSerializer

router = routers.DefaultRouter()
router.register(r'place', PlaceViewSet)


app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(),name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
    path('map/', views.MapDetail, name="map"),
]
