from django.contrib import admin
from .models import URL

@admin.register(URL)
class urls(admin.ModelAdmin):
    list_display = ('id' ,'url', 'shortcode', 'count')
    ordering = ('id',)
    search_fields = ('url',)

# Another method :-
# admin.site.register(URL)
