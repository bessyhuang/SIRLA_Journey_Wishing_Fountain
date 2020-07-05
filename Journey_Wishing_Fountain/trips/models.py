from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	location = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=12)
	tag = models.CharField(max_length=10)
	photo = models.URLField(blank = True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True) 

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

'''
author 			作者
title			標題
text 			介紹景點的內容
location 		地點
phone_number 	
tag				標籤
photo			照片(格式是圖片網址)
created_date
published_date
'''