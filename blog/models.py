from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    #작성 시각, 수정 시각 자동 설정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'