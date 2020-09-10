from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.shortcuts import reverse
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=80,verbose_name="Başlık")

    def __str__(self):
        return self.name
    
class Articles(models.Model):
    



    title=models.CharField(max_length=80,verbose_name="Başlık")
    article_img = models.FileField(blank=True,null=True,verbose_name="Görsel")
    content=RichTextField()
    add_date=models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=300,unique=True,null=False)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    #category=models.CharField(max_length=80,verbose_name="Kategori",choices=[('green', 'green'), ('red', 'red')])
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Kategory")
    likes=models.ManyToManyField("auth.User",related_name="likes",blank=True)
    cc=models.ManyToManyField("auth.User",related_name="cc",blank=True)
    def __str__(self):
        return self.title

    def totalLike(self):
        return self.likes
    
    def totalcc(self):
        return self.cc
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['-add_date']
    

class Comments(models.Model):
    article=models.ForeignKey(Articles,verbose_name="Makale",on_delete=models.CASCADE,related_name="comments")
    commet_author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    commet_content=models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']


class Visit(models.Model):
    arti=models.ForeignKey(Articles,verbose_name="Makale",on_delete=models.CASCADE,related_name="view")
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)




   
"""class Commander(models.Model):
    article=models.ForeignKey(Articles,verbose_name="Makale",on_delete=models.CASCADE,related_name="comments")
    commentauthor=models.ManyToManyField("auth.User")
    commentcontent=models.CharField(max_length=200,verbose_name="Yorum")
    commentdate=models.DateTimeField(auto_now_add=True)"""

    

