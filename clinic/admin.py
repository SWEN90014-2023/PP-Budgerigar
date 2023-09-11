from django.contrib import admin
from .models import ClinicianInfo
# from .models import AdminInfo
from .models import PatientInfo
from django.contrib.admin import AdminSite
from django.utils.html import format_html



# Register your models here.
admin.site.site_header = "My Clinic Admin"
admin.site.site_title = "My Clinic Admin Portal"
admin.site.index_title = "Welcome to Clinic Researcher Portal"


@admin.register(ClinicianInfo)
class ClinicianInfoAdmin(admin.ModelAdmin):
    list_display = ['cli_id','cli_name']
    search_fields = ['cli_name','cli_id']

    # pass

# @admin.register(AdminInfo)
# class AdminInfoAdmin(admin.ModelAdmin):
#     pass
@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    # pass
    list_display = ['pa_id','cli_id','pa_name','age', 'sex', 'create_time', 'info', 'return_href']

    readonly_fields = ['create_time']

    list_filter = ('sex','age', )

    search_fields = ['pa_name','pa_id']

    ordering = ['pa_id']

    list_per_page = 5

    # #获取保存数据
    # def save_model(self, request, obj, form, change):
    #     if change:
    #         obj.info = obj.info + ' (updated)'
    #     else:
    #         obj.info = obj.info + ' (created)'
    #     super(PatientInfoAdmin,self).save_model(request, obj, form, change)

    #自定义html
    def return_href(self, obj):
        return format_html('<a href="{}"> link', 'https://www.baidu.com')