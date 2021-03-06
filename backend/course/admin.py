from django.contrib import admin
from .models import (
    Recording,
    Category,
    Enrollment,
    SubscriptionType,
    Module,
    Group,
    Course,
    Subscription,
    Event,
)

admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Recording)
admin.site.register(Event)
admin.site.register(Category)

# Register your models here.
