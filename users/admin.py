from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from users.models import User
from .models import Subscriber

from polar_auth.settings import DEFAULT_FROM_EMAIL as from_address


@admin.action(description='Send email')
def admin_email(adminobject, request, queryset):
    if 'apply' in request.POST:
        subject = request.POST['subject']
        message = request.POST['message']
        html_message = request.POST['html_message']
        for object in queryset:
            send_mail(
                subject, message, from_address,
                [object.email],
                html_message=html_message, fail_silently=False,
            )

            object.has_received_email = True
            object.save()

        adminobject.message_user(request, f"Sent email to {queryset.count()} addresses.")
        return HttpResponseRedirect(request.get_full_path())

    context = {'queryset': queryset, 'count': queryset.count()}
    return render(request, 'admin/send_email.html', context=context)


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'consent', 'privacy', 'first_survey_done', 'authorized')
    list_filter = ('email', 'consent', 'privacy', 'first_survey_done', 'authorized')
    fieldsets = (
        (None, {'fields': ('email', 'home_address', 'size', 'consent', 'privacy', 'first_survey_done', 'password', 'user_id', 'authorized')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'home_address', 'size', 'consent', 'privacy', 'first_survey_done', 'password',
                       'is_superuser')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    actions = [admin_email]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class SubscriberAdmin(ModelAdmin):
    model = Subscriber
    list_display = ('email', 'has_received_email')
    list_filter = ('email', 'has_received_email')
    actions = [admin_email]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'has_received_email')}
         ),
    )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(User, CustomUserAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
