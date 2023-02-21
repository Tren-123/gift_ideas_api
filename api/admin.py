from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Gift

admin.site.register(User, UserAdmin)
#admin.site.register(Category)
#admin.site.register(Gift)


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    filter_horizontal = ['category']

class GiftsInline(admin.TabularInline):
    model = Gift.category.through

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        GiftsInline,
    ]
    exclude = ('category',)