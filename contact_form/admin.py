from django.contrib import admin

from contact_form.models import Example


class ExampleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Example, ExampleAdmin)
