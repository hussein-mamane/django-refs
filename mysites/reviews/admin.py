from django.contrib import admin

# Register your models here to work with them from admin.
#  Category, Theme,
from .models import Reviewer, Article, PublicationLink, ImageOrVideo, Section
# admin.site.register(Category)
# admin.site.register(Theme)
admin.site.register(Reviewer)
admin.site.register(Article)
admin.site.register(PublicationLink)
admin.site.register(ImageOrVideo)
admin.site.register(Section)
