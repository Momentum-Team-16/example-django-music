from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Album, Artist, Genre, User

admin.site.register(User, UserAdmin)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
