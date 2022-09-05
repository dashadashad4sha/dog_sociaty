from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category, Doggy
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'is_published', 'photo')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return mark_safe(f'<img src="http://127.0.0.1:8000/media/photos/2022/01/12/IMG-20210819-WA0003.jpg" width="75">')

    get_photo.short_description = 'Мини-фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class DoggyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo', 'poroda')
    list_editable = ('content',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Doggy, DoggyAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
