from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserToken, OrganizationProfile


class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'full_name',)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)




# DOCS - https://docs.djangoproject.com/en/3.1/ref/contrib/admin/

class UserProfileAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'timestamp')

admin.site.register(OrganizationProfile, UserProfileAdmin)


class UserTokenAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'timestamp')

admin.site.register(UserToken,UserTokenAdmin)