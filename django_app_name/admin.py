from django.contrib import admin, messages

from django.http import HttpResponseRedirect
from django.urls import path


class SomeModelAdmin(admin.ModelAdmin):
    change_list_template = 'django_app_name/admin/promo_code_changelist.html'
    list_display = ()

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('url_name/', self.update),
        ]
        return my_urls + urls

    def update(self, request):
        try:
            self.model.update()
            self.message_user(request, "Ok")
        except Exception as e:
            self.message_user(request, str(e), level=messages.ERROR)
        return HttpResponseRedirect("../")
