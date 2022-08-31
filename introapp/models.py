from django.db import models


class donation_organization(models.Model):
    donation_organization = models.TextField(max_length=50, null=True) # 기부단체 이름
    region = models.TextField(max_length=20, null=True) # 읍면동
    latitude = models.FloatField(default=0, null=True) # 위도
    longitude = models.CharField(max_length=20) # 경도
    content = models.TextField(null=True) # 상세내용
