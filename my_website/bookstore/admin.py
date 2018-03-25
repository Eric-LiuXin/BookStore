from django.contrib import admin

# Register your models here.
from .models import Books

class Bookstore(admin.ModelAdmin):
    list_display = ('name', 'intro', 'create_date')

admin.site.register(Books, Bookstore)