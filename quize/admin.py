from django.contrib import admin
from .models import  *
# Register your models here.

admin.site.register(questions)
admin.site.register(answers)
admin.site.register(relation)