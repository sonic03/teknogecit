from django.db import models

# Create your models here.

class Advert(models.Model):
    title=models.CharField(max_length=80,verbose_name="Başlık")
    content=models.TextField(verbose_name="Açıklama")
    add_time=models.DateTimeField(auto_now_add=True)
    is_clicket=models.BooleanField(default=False)
    count=models.IntegerField()
    owner=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    