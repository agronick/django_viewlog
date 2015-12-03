from django.db.models import Count
from models import PageLog
from django.contrib import admin 
from django.views.generic import ListView
from django.conf.urls import patterns

 
    
    
class PageviewSummary(admin.ModelAdmin):
    model = PageLog
    list_display = ['user','path','date','status_code','request_type']
    search_fields = ['user','path','date','status_code','request_type']
    list_filter = ['date','status_code','request_type']
    search_fields = ['user__username','path']
    readonly_fields = [i.name for i in PageLog._meta.fields]
    list_display_links = ['path']
    ordering = ('-date',) 
     
    def has_add_permission(self, request):
        return False
    
admin.site.register(PageLog, PageviewSummary)

 
