from django.contrib import admin
from api_app.models import User,Member,Activity

# Register your models here.
admin.site.register(Member)
admin.site.register(Activity)
admin.site.register(User)