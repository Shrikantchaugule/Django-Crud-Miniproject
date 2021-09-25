from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','roll','year','contact')

#username: crud
#pass : 123