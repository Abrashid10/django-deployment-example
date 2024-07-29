from django.contrib import admin
from myapp.models import Access_Records, Webpage, Topic
# Register your models here.
admin.site.register(Access_Records)
admin.site.register(Webpage)
admin.site.register(Topic)