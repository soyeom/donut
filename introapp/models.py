from django.db import models



class Society(models.Model):
    society = models.TextField(max_length=50, null=True) # 기부단체 이름
    region = models.TextField(max_length=20, null=True) # 읍면동
    latitude = models.CharField(max_length=20) # 위도
    longitude = models.CharField(max_length=20) # 경도
    content = models.TextField(null=True) # 상세내용
