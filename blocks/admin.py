from django.contrib import admin

# Register your models here.
from .models import Profile,Book,Block,BookCategories,College,Comment,CommentRating
admin.site.register(Profile)
admin.site.register(BookCategories)
admin.site.register(Book)
admin.site.register(Block)
admin.site.register(Comment)
admin.site.register(CommentRating)
admin.site.register(College)