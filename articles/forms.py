from django import forms
from .models import Articles,Category

choices=Category.objects.all().values_list("name","name")

choice_list=[]

for i in choices:
    choice_list.append(i)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields=["title","content", "category" ,"article_img"]


        widgets = { 
          "category":forms.Select(choices=choice_list),
    
            }

