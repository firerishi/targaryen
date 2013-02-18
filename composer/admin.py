from composer.models import Post, Page
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'content', 'pub_date')
	fields = ['pub_date', 'content']

class PageAdmin(admin.ModelAdmin):
	list_display = ('id', 'url', 'content', 'pub_date')
	fields = ['pub_date', 'content', 'url']

admin.site.register(Post, PostAdmin)

admin.site.register(Page, PageAdmin)