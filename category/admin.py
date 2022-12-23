from django.contrib import admin

from .models import Category, RootCategory

admin.site.register((Category, RootCategory))
