from accounts.models import CustomUser
from django.db import models
from django.conf import settings

from  django.utils import timezone
import googlemaps
from fansnetworks.local_settings import MAPS_API_KEY
# Create your models here.

import geocoder

def geocode(address):

    ret = geocoder.osm(address, timeout=5.0)
    lat, lng = ret.latlng

    return lat, lng

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Diary(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField('タイトル',max_length= 40)
    date = models.DateField(default=timezone.now)
    address = models.CharField(verbose_name='住所', max_length=100)
    content = models.TextField(verbose_name='本文', blank= True, null= True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self) :
        return self.title


    
    


    
