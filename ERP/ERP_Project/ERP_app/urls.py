from django.urls import path,include

from .views import *
from rest_framework import routers

#######FOR VIEWSET############
router = routers.DefaultRouter()
# router.register(r'receptions' , ReceptionsViewSet ,basename="receptions")

#######FOR APIView############
urlpatterns = [
    path(r'', include(router.urls)),
    path('class/' , Add_class_api.as_view()),
    path('section/' , Section_api.as_view()),
    path('busroot/' , BusRoot_api.as_view()),
    path('hostel/' , Hostel_api.as_view()),
    path('department/' , Department_api.as_view()),
    path('staff/' , Staff_api.as_view()),
    path('school_info/' , SchoolInfo_api.as_view()),
    path('reception/' , Reception_api.as_view()),
    path('admissions_form/' , Admissions_form_api.as_view()),
    path('student_type/' , Student_type_api.as_view()),
    path('extra_fee_structure/' , ExtraFeeStructure_api.as_view()),
    path('extra_fee_discount/' , ExtraFeeDiscount_api.as_view()),
    path('class_fee_discount/' , ClassFeeDiscount_api.as_view()),
    path('reset_class_fee_discount/' , Reset_ClassFeeDiscount_api.as_view()),
    path('hostel_fee_discount/' , HostelFeeDiscount_api.as_view()),
    path('reset_hostel_fee_discount/' , Reset_HostelFeeDiscount_api.as_view()),
    path('bus_fee_discount/' , BusFeeDiscount_api.as_view()),
    path('reset_bus_fee_discount/' , Reset_BusFeeDiscount_api.as_view()),
    path('hostel_extra_fee_structure/' , HostelExtraFeeStructure_api.as_view()),
    path('hostel_extra_fee_discount/' , HostelExtraFeeDiscount_api.as_view()),
    path('genrate_school_fee/' , Genrate_School_Fee_api.as_view()),
    path('genrate_hostel_fee/' , Genrate_Hostel_Fee_api.as_view()),
    path('class_fee_payment/' , Class_Fee_Payment_api.as_view()),
    path('hostel_fee_payment/' , Hostel_Fee_Payment_api.as_view()),



    path('payfee_student_details/' , PayFee_student_details.as_view()),
    path('month_wise_total_fee/' , Month_wise_total_fee_api.as_view()),
    path('one_time_class_fee_payment/' , One_time_class_fee_payment_api.as_view()),
    path('dashboard/' , Dashboard_api.as_view()),






   


]
