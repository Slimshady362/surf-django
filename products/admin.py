from django.contrib import admin
from .models import Topic, Resource,RecommendedResource

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'resource_type', 'url')
    list_filter = ('topic', 'resource_type')

admin.site.register(RecommendedResource)

