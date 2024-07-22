from django.contrib import admin
from .models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name", "phone",
                    "category","owner","picture",]
    
    ordering = ["-id"]
    
    list_filter = ["Created_at",]
    
    search_fields = ["id", "first_name", "last_name",]
    list_per_page = 1
    
@admin.register(Category)   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    
