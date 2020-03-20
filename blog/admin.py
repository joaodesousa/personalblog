from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Post, PostAdmin)