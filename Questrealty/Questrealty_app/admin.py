from django.contrib import admin
from .models import Payment, Review, Message, Room

# Register your models here.
admin.site.register(Payment)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Review)