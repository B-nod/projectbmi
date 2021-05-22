from django.contrib import admin
from useraccount.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "email", "age", "gender", "contact", "address", )