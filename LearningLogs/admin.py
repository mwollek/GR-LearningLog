from django.contrib import admin
import LearningLogs.models as md
# Register your models here.

admin.site.register(md.Topic)
admin.site.register(md.Entry)