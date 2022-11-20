from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import settings_common, settings_dev


from diary.models import Diary

from rest_framework import routers, serializers, viewsets



class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ('title', 'address', 'lat', 'lng')

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = PlaceSerializer

router = routers.DefaultRouter()
router.register(r'customer', PlaceViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
    path('diary/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)

