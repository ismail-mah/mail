from django.contrib import admin

from mail.models import User, Email

# Register your models here.
admin.site.register(User)

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'subject', 'timestamp', 'read', 'archived')
    list_filter = ('read', 'archived', 'timestamp')
    search_fields = ('subject', 'body', 'sender__username', 'recipients__username')