from composer.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	list_display = ('id','content', 'pub_date')
	fields = ['pub_date', 'content']

admin.site.register(Post, PostAdmin)