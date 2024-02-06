from django.contrib import admin
from .models import papers, subjects, years

# Register your models here.
admin.site.register(papers)
admin.site.register(subjects)
admin.site.register(years)
