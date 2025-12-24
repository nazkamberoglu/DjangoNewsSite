from django.contrib import admin

# Register your models here.
from .models import Category
admin.site.register(Category)

from .models import News
admin.site.register(News)

from .models import Horoscope
admin.site.register(Horoscope)

from .models import Blog
admin.site.register(Blog)