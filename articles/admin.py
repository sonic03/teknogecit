from django.contrib import admin
from .models import Articles,Comments,Category,Visit

# Register your models here.

admin.site.register(Visit)
admin.site.register(Comments)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model=Category

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):


    list_display=["title","author","add_date","category"]
    
    prepopulated_fields = {'slug': ('title',)}

    search_fields=["title"]
    list_filter=["add_date","title","category"]
    class Meta:
        model=Articles
        