from django.contrib import admin
from db_app.models import user_table,donation_table,charities_organizations_name,comments_and_feedback

# Register your models here.

admin.site.register(user_table)
admin.site.register(donation_table)
admin.site.register(charities_organizations_name)
admin.site.register(comments_and_feedback)