from django.contrib import admin
from dashboard.models import Wish

def make_open(modeladmin, request, queryset):
    queryset.update(status='open')

def make_in_progress(modeladmin, request, queryset):
    queryset.update(status='in_progress')

def make_done(modeladmin, request, queryset):
    queryset.update(status='done')

def make_done(modeladmin, request, queryset):
	queryset.update(status='close')

class WishAdmin(admin.ModelAdmin):
    fields = ['email','wish','date']
    list_display = ('email','wish','status','date')
    list_filter = ['date']
    actions = [make_open, make_in_progress, make_done]

admin.site.register(Wish, WishAdmin)