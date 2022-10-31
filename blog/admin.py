from django.contrib import admin
from .models import Post, Question
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register((Question))
class QuestionAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approved_questions']

    # def approved_questions(self, request, queryset):
    #     queryset.update(approved=True)
