from django.contrib import admin
from .models import events_info, takePart, contactUs


# Register your models here.
admin.site.register(events_info)
admin.site.register(contactUs)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('user', 'subject',  'descripion', 'document')


admin.site.register(takePart, PostAdmin)

# admin.site.register(users_info)
