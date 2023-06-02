from django.contrib import admin
from ERP_app.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(SchoolInfo)
admin.site.register(AddClass)
admin.site.register(AddHostel)
admin.site.register(BusRoot)
admin.site.register(AddSection)
admin.site.register(Reception)
admin.site.register(Admissions_form)
admin.site.register(AddDepartment)
admin.site.register(AddStaff)
admin.site.register(Student_type)
admin.site.register(ExtraFeeStructure)
admin.site.register(ExtraFeeDiscount)
admin.site.register(ClassFeeDiscount)
admin.site.register(HostelFeeDiscount)
admin.site.register(BusFeeDiscount)
admin.site.register(HostelExtraFeeStructure)
admin.site.register(HostelExtraFeeDiscount)
admin.site.register(Receipt)
admin.site.register(Receipt_for_ExtraFee)
admin.site.register(Hostel_Receipt)

############################################################

# admin.site.register(ExtraFeeStructure)
# admin.site.register(Income)
# admin.site.register(Receipt)
# admin.site.register(ExtraFeeDiscount)
# admin.site.register(HostelReceipt)
# admin.site.register(ExtraFeePaid)

