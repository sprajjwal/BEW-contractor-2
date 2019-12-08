from django.contrib import admin
from blogs.models import Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'modified')


admin.site.register(Page, PageAdmin)
