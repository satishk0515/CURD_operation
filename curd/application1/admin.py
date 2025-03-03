from django.contrib import admin
from .models import user

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=('id','Name','Email','Password')




# Register your models here.

# class useradmin(admin.ModelAdmin):
#     list_display=[,'name','email','password']


# admin.site.register(user,useradmin)