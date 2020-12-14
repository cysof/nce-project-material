from django.contrib import admin
from blog.models import Post, Category
from django.contrib.auth.models import Group

class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = 'CYSOFT-HOME'
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)
