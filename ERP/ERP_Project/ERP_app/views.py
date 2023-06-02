
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets  , serializers,permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from url_filter.integrations.drf import DjangoFilterBackend
import django_filters.rest_framework
from rest_framework.response import Response
from titlecase import titlecase
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.core.mail import EmailMessage
import random
from rest_framework import status

# Create your views here.
class Add_class_api(APIView):
    def get(self, request):
        class_name = self.request.query_params.get('class_name')
        print(class_name,'ll')
        if(class_name):
            class_details = AddClass.objects.filter(class_name=class_name).values()
        else:
            class_details = AddClass.objects.all().values()
        return Response({'res':class_details})

    def post(self, request):
        data=request.data
        class_name=data.get('class_name')
        year=data.get('year')
        class_fee=data.get('class_fee')
        class_fee_inst=data.get('class_fee_inst')
        print(data,'data')
        class_create= AddClass.objects.create(year=year,class_name=class_name,class_fee=class_fee,class_fee_inst=class_fee_inst)
        return Response({'messages':"Class Created Successfully!",'status':status.HTTP_201_CREATED})

class Section_api(APIView):
    def get(self, request):
        section_details = AddSection.objects.all().values()
        return Response({'res':section_details})

    def post(self, request):
        data=request.data
        section_name=data.get('section_name')
        section_create= AddSection.objects.create(section_name=section_name)
        return Response({'messages':"Section Created Successfully!",'status':status.HTTP_201_CREATED})

class BusRoot_api(APIView):
    def get(self, request):
        bus_root_details = BusRoot.objects.all().values()
        return Response({'res':bus_root_details})

    def post(self, request):
        data=request.data
        bus_name=data.get('bus_name')
        year=data.get('year')
        root_name=data.get('root_name')
        root_fee=data.get('root_fee')
        root_inst=data.get('root_inst')
        bus_root_create= BusRoot.objects.create(year=year,bus_name=bus_name,root_name=root_name,root_fee=root_fee,root_inst=root_inst)
        return Response({'messages':"Bus Root Created Successfully!",'status':status.HTTP_201_CREATED})

class Hostel_api(APIView):
    def get(self, request):
        hostel_details = AddHostel.objects.all().values()
        return Response({'res':hostel_details})

    def post(self, request):
        data=request.data
        year=data.get('year')
        hostel_name=data.get('hostel_name')
        hostel_fee=data.get('hostel_fee')
        hostel_fee_inst=data.get('hostel_fee_inst')
        hostel_instruction=data.get('hostel_instruction')
        
        hostel_create= AddHostel.objects.create(year=year,hostel_name=hostel_name,hostel_fee=hostel_fee,hostel_fee_inst=hostel_fee_inst,hostel_instruction=hostel_instruction)
        return Response({'messages':"Hostel Created Successfully!",'status':status.HTTP_201_CREATED})

class Department_api(APIView):
    def get(self, request):
        department_details = AddDepartment.objects.all().values()
        return Response(department_details)

    def post(self, request):
        data=request.data
        department_name=data.get('department_name')
        department_create= AddDepartment.objects.create(department_name=department_name)
        return Response({'messages':"department created successfully!!!",'status':status.HTTP_201_CREATED})

class Staff_api(APIView):
    def get(self, request):
        staff_details = AddStaff.objects.all().values()
        return Response(staff_details)

    def post(self, request):
        data=request.data
        department_id=data.get('department_id')
        staff_name=data.get('staff_name')
        date_of_birth=data.get('date_of_birth')
        email=data.get('email')
        mobile_no=data.get('mobile_no')
        gender=data.get('gender')
        joining_date=data.get('joining_date')
        designation=data.get('designation')
        basic_salary=data.get('basic_salary')
        subject=data.get('subject')
        father_name=data.get('father_name')
        mother_name=data.get('mother_name')
        husband_name=data.get('husband_name')
        staff_qualification=data.get('staff_qualification')
        temp_address=data.get('temp_address')
        permanent_address=data.get('permanent_address')
        alternate_mobile_no=data.get('alternate_mobile_no')
        staff_create= AddStaff.objects.create(
                                department_id=department_id,
                                staff_name=staff_name,
                                date_of_birth=date_of_birth,
                                email=email,
                                mobile_no=mobile_no,
                                gender=gender,
                                joining_date=joining_date,
                                designation=designation,
                                basic_salary=basic_salary,
                                subject=subject,
                                father_name=father_name,
                                mother_name=mother_name,
                                husband_name=husband_name,
                                staff_qualification=staff_qualification,
                                temp_address=temp_address,
                                permanent_address=permanent_address,
                                alternate_mobile_no=alternate_mobile_no)
        return Response({'messages':"staff created successfully!!!",'status':status.HTTP_201_CREATED})

class SchoolInfo_api(APIView):
    def get(self, request):
        schoolinfo_details = SchoolInfo.objects.all().values()
        return Response(schoolinfo_details)

    def post(self, request):
        data=request.data
        school_name=data.get('school_name')
        school_address1=data.get('school_address1')
        school_address2=data.get('school_address2')
        school_mobile1=data.get('school_mobile1')
        school_mobile2=data.get('school_mobile2')
        school_email=data.get('school_email')
        school_web=data.get('school_web')
        school_img=data.get('school_img')
        school_logo=data.get('school_logo')

        school_info_create=SchoolInfo.objects.create(
                school_name=school_name,
                school_address1=school_address1,
                school_address2=school_address2,
                school_mobile1=school_mobile1,
                school_mobile2=school_mobile2,
                school_email=school_email,
                school_web=school_web,
                school_img=school_img,
                school_logo=school_logo
                )
       
        return Response({'messages':"school_info created successfully!!!",'status':status.HTTP_201_CREATED})

class Reception_api(APIView):
    def get(self, request):
        reception_details = Reception.objects.all().values()
        return Response(reception_details)

    def post(self, request):
        data=request.data
        student_name=data.get('student_name')
        class_id=data.get('class_id')
        gender=data.get('gender')
        date_of_enq=data.get('date_of_enq')
        date_of_birth=data.get('date_of_birth')
        father_name=data.get('father_name')
        mother_name=data.get('mother_name')
        father_mobile_no=data.get('father_mobile_no')
        mother_mobile_no=data.get('mother_mobile_no')
        temp_address=data.get('temp_address')
        permanent_address=data.get('permanent_address')
        testDate=data.get('testDate')
        testTime=data.get('testTime')
        print(data,'data')

        # reception_create= Reception.objects.create(date_of_enq=date_of_enq,
        #     student_name=student_name,
        #     class_name_id=class_id,
        #     gender=gender,
        #     date_of_birth=date_of_birth,
        #     father_name=father_name,
        #     mother_name=mother_name,
        #     father_mobile_no=father_mobile_no,
        #     mother_mobile_no=mother_mobile_no,
        #     temp_address=temp_address,
        #     permanent_address=permanent_address,
        #     testDate=testDate,
        #     testTime=testTime

        # )
        return Response({'messages':"reception created successfully!!!",'status':status.HTTP_201_CREATED})

class Admissions_form_api(APIView):
    def get(self, request):
        admission_id = self.request.query_params.get('admission_id')
        arr=[]
        if(admission_id):
            admissions_details = Admissions_form.objects.filter(id=admission_id,is_active=True)
            for i in admissions_details:
                arr.append({
                    'id':i.id,
                    'reception_id':i.reception_id,
                    "student_name":i.reception.student_name,
                    "class_name":i.reception.class_name.class_name,
                    "gender":i.reception.gender,
                    "date_of_birth":i.reception.date_of_birth,
                    "father_name":i.reception.father_name,
                    "mother_name":i.reception.mother_name,
                    "father_mobile_no":i.reception.father_mobile_no,
                    "mother_mobile_no":i.reception.mother_mobile_no,
                    "temp_address":i.reception.temp_address,
                    "permanent_address":i.reception.permanent_address,
                    'bus_root_id':i.bus_root_id,
                    "bus_name":i.bus_root.bus_name,
                    "root_name":i.bus_root.root_name,
                    "root_fee":i.bus_root.root_fee,
                    "root_inst":i.bus_root.root_inst,
                    'section_id':i.section_id,
                    "section_name":i.section.section_name,
                    'hostel_id':i.hostel_id,
                    "hostel_name":i.hostel.hostel_name,
                    "student_type_id":i.student_type_id,
                    "student_type_name":i.student_type.student_type_name,
                    "hostel_fee":i.hostel.hostel_fee,
                    "hostel_fee_inst":i.hostel.hostel_fee_inst,
                    "hostel_instruction":i.hostel.hostel_instruction,
                    'admission_date':i.admission_date,
                    'admission_no':i.admission_no,
                    'roll_no':i.roll_no,
                    'caste':i.caste,
                    'religion':i.religion,
                    'father_occupation':i.father_occupation,
                    'father_qualification':i.father_qualification,
                    'alternate_mobile_no':i.alternate_mobile_no,
                    'mother_occupation':i.mother_occupation,
                    'mother_qualification':i.mother_qualification,
                    'studentImage':str(i.studentImage),
                    'studentAadhar':str(i.studentAadhar),
                    'studentDOBCerficate':str(i.studentDOBCerficate),
                    'studentTC':str(i.studentTC)
                })
        else:    
            admissions_details = Admissions_form.objects.filter()
            for i in admissions_details:
                arr.append({
                    'id':i.id,
                    'reception_id':i.reception_id,
                    "student_name":i.reception.student_name,
                    "class_name":i.reception.class_name.class_name,
                    "gender":i.reception.gender,
                    "date_of_birth":i.reception.date_of_birth,
                    "father_name":i.reception.father_name,
                    "mother_name":i.reception.mother_name,
                    "father_mobile_no":i.reception.father_mobile_no,
                    "mother_mobile_no":i.reception.mother_mobile_no,
                    "temp_address":i.reception.temp_address,
                    "permanent_address":i.reception.permanent_address,
                    'bus_root_id':i.bus_root_id,
                    "bus_name":i.bus_root.bus_name,
                    "root_name":i.bus_root.root_name,
                    "root_fee":i.bus_root.root_fee,
                    "root_inst":i.bus_root.root_inst,
                    'section_id':i.section_id,
                    "section_name":i.section.section_name,
                    'hostel_id':i.hostel_id,
                    "hostel_name":i.hostel.hostel_name,
                    "student_type_id":i.student_type_id,
                    "student_type_name":i.student_type.student_type_name,
                    "hostel_fee":i.hostel.hostel_fee,
                    "hostel_fee_inst":i.hostel.hostel_fee_inst,
                    "hostel_instruction":i.hostel.hostel_instruction,
                    'admission_date':i.admission_date,
                    'admission_no':i.admission_no,
                    'roll_no':i.roll_no,
                    'caste':i.caste,
                    'religion':i.religion,
                    'father_occupation':i.father_occupation,
                    'father_qualification':i.father_qualification,
                    'alternate_mobile_no':i.alternate_mobile_no,
                    'mother_occupation':i.mother_occupation,
                    'mother_qualification':i.mother_qualification,
                    'studentImage':str(i.studentImage),
                    'studentAadhar':str(i.studentAadhar),
                    'studentDOBCerficate':str(i.studentDOBCerficate),
                    'studentTC':str(i.studentTC)

                })

        return Response({'res':arr})

    def post(self, request):
        data=request.data
        reception_id=data.get('reception_id')
        bus_root_id=data.get('bus_root_id')
        section_id=data.get('section_id')
        hostel_id=data.get('hostel_id')
        student_type_id=data.get('student_type_id')
        admission_date=data.get('admission_date')
        admission_no=data.get('admission_no')
        roll_no=data.get('roll_no')
        caste=data.get('caste')
        religion=data.get('religion')
        father_occupation=data.get('father_occupation')
        father_qualification=data.get('father_qualification')
        alternate_mobile_no=data.get('alternate_mobile_no')
        mother_occupation=data.get('mother_occupation')
        mother_qualification=data.get('mother_qualification')
        alternate_mobile_no=data.get('alternate_mobile_no')
        studentImage=data.get('studentImage')
        studentAadhar=data.get('studentAadhar')
        studentDOBCerficate=data.get('studentDOBCerficate')
        studentTC=data.get('studentTC')

        admission_create= Admissions_form.objects.create( reception_id=reception_id,
                bus_root_id=bus_root_id,
                section_id=section_id,
                hostel_id=hostel_id,
                student_type_id=student_type_id,
                admission_date=admission_date,
                admission_no=admission_no,
                roll_no=roll_no,
                caste=caste,
                religion=religion,
                father_occupation=father_occupation,
                father_qualification=father_qualification,
                alternate_mobile_no=alternate_mobile_no,
                mother_occupation=mother_occupation,
                mother_qualification=mother_qualification,
                studentImage=studentImage,
                studentAadhar=studentAadhar,
                studentDOBCerficate=studentDOBCerficate,
                studentTC=studentTC
                )

        return Response({'messages':"Admission form submited successfully!!!",'status':status.HTTP_201_CREATED})

class Student_type_api(APIView):
    def get(self, request):
        student_type_details = Student_type.objects.all().values()
        return Response({'res':student_type_details})

    def post(self, request):
        data=request.data
        student_type_name=data.get('student_type_name')
        student_type_create= Student_type.objects.create(student_type_name=student_type_name)
        return Response({'messages':"student_type created successfully!!!",'status':status.HTTP_201_CREATED})

class ExtraFeeStructure_api(APIView):
    def get(self, request):
        class_id = self.request.query_params.get('class_id')
        student_type_id = self.request.query_params.get('student_type_id')
        arr=[]
        if(class_id and student_type_id):
            extraFeeStructure_details = ExtraFeeStructure.objects.filter(class_name__id=class_id,student_type__id=student_type_id)
            for i in extraFeeStructure_details:
                arr.append({
                    'id':i.id,
                    'class_name_id':i.class_name_id,
                    "class_name":i.class_name.class_name,
                    'student_type_id':i.student_type_id,
                    "student_type_name":i.student_type.student_type_name,
                    "fee_name":i.fee_name,
                    "fee_amount":i.fee_amount,
                    "month":i.month,
                    "year":i.year
                })
        else:
            extraFeeStructure_details = ExtraFeeStructure.objects.all()
            for i in extraFeeStructure_details:
                arr.append({
                    'id':i.id,
                    'class_name_id':i.class_name_id,
                    "class_name":i.class_name.class_name,
                    'student_type_id':i.student_type_id,
                    "student_type_name":i.student_type.student_type_name,
                    "fee_name":i.fee_name,
                    "fee_amount":i.fee_amount,
                    "month":i.month,
                    "year":i.year
                })
        return Response({'res':arr})

    def post(self, request):
        data=request.data
        class_id=data.get('class_id')
        student_type_id=data.get('student_type_id')
        fee_name=data.get('fee_name')
        fee_amount=data.get('fee_amount')
        month=data.get('month')
        year=data.get('year')
        extraFeeStructure_create= ExtraFeeStructure.objects.create(class_name_id=class_id,
                                    student_type_id=student_type_id,
                                    fee_name=fee_name,fee_amount=fee_amount,
                                    month=month,year=year)
                                
        return Response({'messages':"extraFeeStructure created successfully!!!",'status':status.HTTP_201_CREATED})

class ExtraFeeDiscount_api(APIView):
    def get(self, request):
        extraFeeDiscount_details = ExtraFeeDiscount.objects.all().values()
        return Response(extraFeeDiscount_details)
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        extra_fee_structure_id=data.get('extra_fee_structure_id')
        discount_name=data.get('discount_name')
        # month=data.get('month')
        # main_amount=data.get('main_amount')
        discounted_amount=data.get('discounted_amount')
        # final_amount=data.get('final_amount')
        main_amount=0
        final_amount=0
        month=''
        extra_fee_structure=ExtraFeeStructure.objects.get(id=extra_fee_structure_id)
        main_amount=extra_fee_structure.fee_amount
        final_amount=int(main_amount)-int(discounted_amount)
        month=extra_fee_structure.month
        year=extra_fee_structure.year

        extraFeeDiscount_create= ExtraFeeDiscount.objects.create(admission_id=admission_id,
                                    extra_fee_structure_id=extra_fee_structure_id,
                                    discount_name=discount_name,
                                    discounted_amount=discounted_amount,
                                    month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')

                                   
        return Response({'messages':"extraFeeDiscount created successfully!!!",'status':status.HTTP_201_CREATED})

class ClassFeeDiscount_api(APIView):
    def get(self, request):
        classFeeDiscount_details = ClassFeeDiscount.objects.all().values()
        return Response(classFeeDiscount_details)
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        discount_name=data.get('discount_name')
        month=data.get('month')
        year=data.get('year')
        # main_amount=data.get('main_amount')
        discounted_amount=data.get('discounted_amount')
        # final_amount=data.get('final_amount')
        main_amount=0
        final_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id

        class_fee_table=AddClass.objects.get(id=class_id)
        main_amount=float(class_fee_table.class_fee)/float(class_fee_table.class_fee_inst)
        final_amount=int(main_amount)-int(discounted_amount)
        if ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month).exists():
            extraFeeDiscount_update= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month).update(status='in-active')
            # extraFeeDiscount_update= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month).update(discount_name=discount_name,
            #                                                                                         discounted_amount=discounted_amount,
            #                                                                                         final_amount=final_amount,status='active')
            extraFeeDiscount_create= ClassFeeDiscount.objects.create(admission_id=admission_id,
                                        discount_name=discount_name,
                                        discounted_amount=discounted_amount,
                                        month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
            return Response({'messages':"ClassFeeDiscount updated successfully!!!",'status':status.HTTP_201_CREATED})
        else:
            extraFeeDiscount_create= ClassFeeDiscount.objects.create(admission_id=admission_id,
                                        discount_name=discount_name,
                                        discounted_amount=discounted_amount,
                                        month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
            return Response({'messages':"extraFeeDiscount created successfully!!!",'status':status.HTTP_201_CREATED})

class Reset_ClassFeeDiscount_api(APIView):
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        month=data.get('month')
        year=data.get('year')
        main_amount=0
        final_amount=0
        discounted_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id

        class_fee_table=AddClass.objects.get(id=class_id)
        main_amount=float(class_fee_table.class_fee)/float(class_fee_table.class_fee_inst)
        final_amount=int(main_amount)-int(discounted_amount)
        if ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).exists():
            classFeeDiscount_update= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).update(discount_name='',
                                                                                                    discounted_amount=discounted_amount,
                                                                                                    final_amount=final_amount)
            return Response({'messages':"classFeeDiscount reset successfully!!!",'status':status.HTTP_201_CREATED})
        else:
                return Response({'messages':"This month no discount for this student!!!",'status':status.HTTP_201_CREATED})

class HostelFeeDiscount_api(APIView):
    def get(self, request):
        hostelFeeDiscount_details = HostelFeeDiscount.objects.all().values()
        return Response(hostelFeeDiscount_details)
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        discount_name=data.get('discount_name')
        month=data.get('month')
        year=data.get('year')
        # main_amount=data.get('main_amount')
        discounted_amount=data.get('discounted_amount')
        # final_amount=data.get('final_amount')
        main_amount=0
        final_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        if(admission_form_table.hostel):
            hostel_fee_table=AddHostel.objects.get(id=admission_form_table.hostel_id)
            main_amount=float(hostel_fee_table.hostel_fee)/float(hostel_fee_table.hostel_fee_inst)
            final_amount=int(main_amount)-int(discounted_amount)

            if HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).exists():
                hostelFeeDiscount_update= HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).update(status='in-active')
                # hostelFeeDiscount_update= HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month).update(discount_name=discount_name,
                #                                                                                         discounted_amount=discounted_amount,
                #                                                                                         final_amount=final_amount)
                hostelFeeDiscount_create= HostelFeeDiscount.objects.create(admission_id=admission_id,
                                            discount_name=discount_name,
                                            discounted_amount=discounted_amount,
                                            month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
                return Response({'messages':"HostelFeeDiscount updated successfully!!!",'status':status.HTTP_201_CREATED})
            else:
                hostelFeeDiscount_create= HostelFeeDiscount.objects.create(admission_id=admission_id,
                                            discount_name=discount_name,
                                            discounted_amount=discounted_amount,
                                            month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
                return Response({'messages':"extraFeeDiscount created successfully!!!",'status':status.HTTP_201_CREATED})

class Reset_HostelFeeDiscount_api(APIView):
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        month=data.get('month')
        year=data.get('year')
        main_amount=0
        final_amount=0
        discounted_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        if(admission_form_table.hostel):
            hostel_fee_table=AddHostel.objects.get(id=admission_form_table.hostel_id)
            main_amount=float(hostel_fee_table.hostel_fee)/float(hostel_fee_table.hostel_fee_inst)
            final_amount=int(main_amount)-int(discounted_amount)
            if HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).exists():
                hostelFeeDiscount_update= HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).update(discount_name='',
                                                                                                        discounted_amount=discounted_amount,
                                                                                                        final_amount=final_amount)
                return Response({'messages':"hostelFeeDiscount_update reset successfully!!!",'status':status.HTTP_201_CREATED})
            else:
                return Response({'messages':"This month no discount for this student!!!",'status':status.HTTP_201_CREATED})

class BusFeeDiscount_api(APIView):
    def get(self, request):
        busFeeDiscount_details = BusFeeDiscount.objects.all().values()
        return Response(busFeeDiscount_details)
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        discount_name=data.get('discount_name')
        month=data.get('month')
        year=data.get('year')
        # main_amount=data.get('main_amount')
        discounted_amount=data.get('discounted_amount')
        # final_amount=data.get('final_amount')
        main_amount=0
        final_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        if(admission_form_table.bus_root):
            bus_fee_table=BusRoot.objects.get(id=admission_form_table.bus_root_id)
            main_amount=float(bus_fee_table.root_fee)/float(bus_fee_table.root_inst)
            final_amount=int(main_amount)-int(discounted_amount)

            if BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).exists():
                busFeeDiscount_update= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month).update(status='in-active')
                # busFeeDiscount_update= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month).update(discount_name=discount_name,
                #                                                                                         discounted_amount=discounted_amount,
                #                                                                                         final_amount=final_amount)
                busFeeDiscount_create= BusFeeDiscount.objects.create(admission_id=admission_id,
                                            discount_name=discount_name,
                                            discounted_amount=discounted_amount,
                                            month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
                return Response({'messages':"busFeeDiscount updated successfully!!!",'status':status.HTTP_201_CREATED})
            else:
                busFeeDiscount_create= BusFeeDiscount.objects.create(admission_id=admission_id,
                                            discount_name=discount_name,
                                            discounted_amount=discounted_amount,
                                            month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
                return Response({'messages':"busFeeDiscount created successfully!!!",'status':status.HTTP_201_CREATED})

class Reset_BusFeeDiscount_api(APIView):
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        month=data.get('month')
        year=data.get('year')
        main_amount=0
        final_amount=0
        discounted_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        if(admission_form_table.bus_root):
            bus_fee_table=BusRoot.objects.get(id=admission_form_table.bus_root_id)
            main_amount=float(bus_fee_table.root_fee)/float(bus_fee_table.root_inst)
            final_amount=int(main_amount)-int(discounted_amount)
            if BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year).exists():
                busFeeDiscount_update= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month).update(discount_name='',
                                                                                                        discounted_amount=discounted_amount,
                                                                                                        final_amount=final_amount)
                return Response({'messages':"busFeeDiscount reset successfully!!!",'status':status.HTTP_201_CREATED})
            else:
                return Response({'messages':"This month no discount for this student!!!",'status':status.HTTP_201_CREATED})

class HostelExtraFeeStructure_api(APIView):
    def get(self, request):
        student_type_id = self.request.query_params.get('student_type_id')
        arr=[]
        if(student_type_id):
            hostel_extraFeeStructure_details = HostelExtraFeeStructure.objects.filter(student_type__id=student_type_id)
            for i in hostel_extraFeeStructure_details:
                arr.append({
                    'id':i.id,
                    'student_type_id':i.student_type_id,
                    "student_type_name":i.student_type.student_type_name,
                    "fee_name":i.fee_name,
                    "fee_amount":i.fee_amount,
                    "month":i.month,
                    "year":i.year,
                })
        else:
            hostel_extraFeeStructure_details = HostelExtraFeeStructure.objects.all()
            for i in hostel_extraFeeStructure_details:
                arr.append({
                    'id':i.id,
                    'student_type_id':i.student_type_id,
                    "student_type_name":i.student_type.student_type_name,
                    "fee_name":i.fee_name,
                    "fee_amount":i.fee_amount,
                    "month":i.month,
                    "year":i.year,
                })
        return Response({'res':arr})

    def post(self, request):
        data=request.data
        student_type_id=data.get('student_type_id')
        fee_name=data.get('fee_name')
        fee_amount=data.get('fee_amount')
        month=data.get('month')
        year=data.get('year') 
        extraFeeStructure_create= HostelExtraFeeStructure.objects.create(student_type_id=student_type_id,
                                    fee_name=fee_name,fee_amount=fee_amount,
                                    month=month,year=year)
        return Response({'messages':"extraFeeStructure created successfully!!!",'status':status.HTTP_201_CREATED})

class HostelExtraFeeDiscount_api(APIView):
    def get(self, request):
        hostelextraFeeDiscount_details = HostelExtraFeeDiscount.objects.all().values()
        return Response(hostelextraFeeDiscount_details)
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        hostel_extra_fee_structure_id=data.get('hostel_extra_fee_structure_id')
        discount_name=data.get('discount_name')
        # month=data.get('month')
        # main_amount=data.get('main_amount')
        discounted_amount=data.get('discounted_amount')
        # final_amount=data.get('final_amount')
        main_amount=0
        final_amount=0
        month=''
        hostel_extra_fee_structure=HostelExtraFeeStructure.objects.get(id=hostel_extra_fee_structure_id)
        main_amount=hostel_extra_fee_structure.fee_amount
        final_amount=int(main_amount)-int(discounted_amount)
        month=hostel_extra_fee_structure.month
        year=hostel_extra_fee_structure.year

        hostelextraFeeDiscount_create= HostelExtraFeeDiscount.objects.create(admission_id=admission_id,
                                    hostel_extra_fee_structure_id=hostel_extra_fee_structure_id,
                                    discount_name=discount_name,
                                    discounted_amount=discounted_amount,
                                    month=month,year=year,main_amount=main_amount,final_amount=final_amount,status='active')
        return Response({'messages':"hostelextraFeeDiscount created successfully!!!",'status':status.HTTP_201_CREATED})

class Genrate_School_Fee_api(APIView):
    def get(self, request):
        admission_id = self.request.query_params.get('admission_id')
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        bus_root_charges=0
        class_charges=0
        total_extra_fee=0
        total_amount=0
        arr=[]
        class_dues=0
        bus_dues=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id
        if Receipt.objects.filter(admission_id=admission_id,month=month,year=year).exists():
            exists_receipt=Receipt.objects.filter(admission_id=admission_id,month=month,year=year).last()
            class_dues=exists_receipt.class_dues
            bus_dues=exists_receipt.bus_dues
    #####################################BUS DUES####################################################################
            if(admission_form_table.bus_root):
                bus_fee_discount_table= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
                if(bus_fee_discount_table):
                    bus_fee_discount_table1= BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    discounted_amount=float(bus_fee_discount_table1.discounted_amount)
                    bus_dues=float(bus_dues)-float(discounted_amount) 
    ########################################CLASS DUES####################################################################
            class_fee_discount_table= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
            if(class_fee_discount_table):
                class_fee_discount_table1= ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                discounted_amount=float(class_fee_discount_table1.discounted_amount)
                class_dues=float(class_dues)-float(discounted_amount) 

    #############################################Extra Fee##################################################################
            
            total_amount=float(class_dues)+float(bus_dues)
            
            res= {}
            res['class_charge']=class_dues
            res['bus_root_charge']=bus_dues
            res['extra_charge']=[]
            res['final_amount']=''  

            if Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt).exists():
                extra_fee_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,month=month,year=year,student_type_id=admission_form_table.student_type_id)
                if(extra_fee_table):
                    for i in extra_fee_table:
                        extra_fee_discount_table= ExtraFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,extra_fee_structure_id=i.id,status='active')
                        if(extra_fee_discount_table):
                            for k in extra_fee_discount_table:
                                fee_id=k.extra_fee_structure.id
                                discounted_amount=k.discounted_amount
                                final_amount=k.final_amount
                                receipt_for_extrafee_exits_table=Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt,extra_fee_structure_id=fee_id)
                                if receipt_for_extrafee_exits_table:
                                    receipt_for_extrafee_exits_table1=Receipt_for_ExtraFee.objects.get(receipt_id=exists_receipt,extra_fee_structure_id=fee_id)
                                    extra_fee_dues=receipt_for_extrafee_exits_table1.extra_fee_dues
                                    total_extra_fee=total_extra_fee+(float(extra_fee_dues)-float(discounted_amount))
                                    res['extra_charge'].append({
                                        "id":i.id,
                                        "fee_name":i.fee_name,
                                        "fee_amount":float(extra_fee_dues)-float(discounted_amount)
                                    })
                                else:    
                                    fee_name=k.extra_fee_structure.fee_name
                                    main_amount=k.main_amount
                                    final_amount=k.final_amount
                                    total_extra_fee=total_extra_fee+int(final_amount)
                                    res['extra_charge'].append({
                                        "id":k.extra_fee_structure.id,
                                        "fee_name":fee_name,
                                        "fee_amount":final_amount
                                    })
                        else:
                            receipt_for_extrafee_exits_table=Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt,extra_fee_structure_id=i.id)
                            if receipt_for_extrafee_exits_table:
                                for l in receipt_for_extrafee_exits_table:
                                    if l.extra_fee_name == i.fee_name:
                                        total_extra_fee=total_extra_fee+float(l.extra_fee_dues)
                                        res['extra_charge'].append({
                                            "id":l.extra_fee_structure.id,
                                            "fee_name":l.extra_fee_name,
                                            "fee_amount":l.extra_fee_dues
                                        })
                            else:
                                total_extra_fee=total_extra_fee+float(i.fee_amount)
                                res['extra_charge'].append({
                                    "id":i.id,
                                    "fee_name":i.fee_name,
                                    "fee_amount":i.fee_amount
                                })
                    res['final_amount']= total_extra_fee+total_amount 
                    arr.append(res)
                    class_arr=[]
                    bus_arr=[]
                    extra_fee_arr=[]
                    total_amount=[]
                    final_arr=[]
                    final_amt_arr=[]
                    for i in arr:
                        class_arr.append({
                            'id':'',
                            'fee_name':'class_charge',
                            "fee_amount":i['class_charge']
                            })
                        bus_arr.append({
                            'id':'',
                            'fee_name':'bus_root_charge',
                            "fee_amount":i['bus_root_charge'],
                        }) 
                        extra_fee_arr.append(i['extra_charge'])  
                        total_amount.append({'final_amount':i['final_amount']}) 
                    
                    final_arr=class_arr+bus_arr+extra_fee_arr[0]
                    return Response({'res':final_arr,'final_amount':total_amount}) 
                    # return Response(arr)
                else:  
                    receipt_for_extrafee_exits_table=Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt)
                    for l in receipt_for_extrafee_exits_table:
                        total_extra_fee=total_extra_fee+float(l.extra_fee_dues)
                        res['extra_charge'].append({
                            "id":l.extra_fee_structure.id,
                            "fee_name":l.extra_fee_name,
                            "fee_amount":l.extra_fee_dues
                        })
                    res['final_amount']=float(total_extra_fee)+float(total_amount) 
                    arr.append(res)
                    class_arr=[]
                    bus_arr=[]
                    extra_fee_arr=[]
                    total_amount=[]
                    final_arr=[]
                    final_amt_arr=[]
                    for i in arr:
                        class_arr.append({
                            'id':'',
                            'fee_name':'class_charge',
                            "fee_amount":i['class_charge']
                            })
                        bus_arr.append({
                            'id':'',
                            'fee_name':'bus_root_charge',
                            "fee_amount":i['bus_root_charge'],
                        }) 
                        extra_fee_arr.append(i['extra_charge'])  
                        total_amount.append({'final_amount':i['final_amount']}) 
                    
                    final_arr=class_arr+bus_arr+extra_fee_arr[0]
                    return Response({'res':final_arr,'final_amount':total_amount}) 
                    # return Response(arr)  
                
            else:    
                extra_fee_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,month=month,year=year,student_type_id=admission_form_table.student_type_id)
                if(extra_fee_table):
                    for i in extra_fee_table:
                        extra_fee_discount_table= ExtraFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,extra_fee_structure_id=i.id,status='active')
                        if(extra_fee_discount_table):
                            for k in extra_fee_discount_table:
                                fee_id=k.extra_fee_structure.id
                                fee_name=k.extra_fee_structure.fee_name
                                main_amount=k.main_amount
                                discounted_amount=k.discounted_amount
                                final_amount=k.final_amount
                                total_extra_fee=total_extra_fee+int(final_amount)
                                res['extra_charge'].append({
                                    "id":k.extra_fee_structure.id,
                                    "fee_name":fee_name,
                                    "fee_amount":final_amount
                                })
                        else:        
                            total_extra_fee=total_extra_fee+int(i.fee_amount)
                            res['extra_charge'].append({
                                "id":i.id,
                                "fee_name":i.fee_name,
                                "fee_amount":i.fee_amount
                            })
                    res['final_amount']= total_extra_fee+total_amount 
                    arr.append(res)
                    class_arr=[]
                    bus_arr=[]
                    extra_fee_arr=[]
                    total_amount=[]
                    final_arr=[]
                    final_amt_arr=[]
                    for i in arr:
                        class_arr.append({
                            'id':'',
                            'fee_name':'class_charge',
                            "fee_amount":i['class_charge']
                            })
                        bus_arr.append({
                            'id':'',
                            'fee_name':'bus_root_charge',
                            "fee_amount":i['bus_root_charge'],
                        }) 
                        extra_fee_arr.append(i['extra_charge'])  
                        total_amount.append({'final_amount':i['final_amount']}) 
                    
                    final_arr=class_arr+bus_arr+extra_fee_arr[0]
                    return Response({'res':final_arr,'final_amount':total_amount}) 
                    # return Response(arr)              


            # return Response({
            #     "class_charges":class_dues,
            #     "bus_root_charges":bus_dues,
            #     "final_amount":total_amount
            #  })
            class_arr=[]
            bus_arr=[]
            final_arr=[]
            total_amounts=[]
            class_arr.append({
                'id':'',
                'fee_name':'class_charge',
                "fee_amount":class_dues
                })
            bus_arr.append({
                'id':'',
                'fee_name':'bus_root_charge',
                "fee_amount":bus_dues,
            }) 
            final_arr=class_arr+bus_arr
            total_amounts.append({'final_amount':total_amount})
            return Response({'res':final_arr,'final_amount':total_amounts})  

        else:
            ###########################bus Fee#####################
            if(admission_form_table.bus_root):
                bus_fee_discount_table= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
                if(bus_fee_discount_table):
                    bus_fee_discount_table1= BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    bus_root_charges=float(bus_fee_discount_table1.final_amount) 
                else:
                    bus_root_id=admission_form_table.bus_root_id
                    bus_root_table=BusRoot.objects.get(id=bus_root_id)
                    bus_root_charges=float(bus_root_table.root_fee)/float(bus_root_table.root_inst)
        
            ##################class Fee####################
            class_fee_discount_table= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
            if(class_fee_discount_table):
                class_fee_discount_table1= ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                class_charges=float(class_fee_discount_table1.final_amount) 
            else:
                class_table=AddClass.objects.get(id=class_id)
                class_charges=float(class_table.class_fee)/float(class_table.class_fee_inst)

            ##################Extra Fee####################
            
            total_amount=class_charges+bus_root_charges
            res= {}
            res['class_charge']=class_charges
            res['bus_root_charge']=bus_root_charges
            res['extra_charge']=[]
            res['final_amount']=''

            extra_fee_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,month=month,year=year,student_type_id=admission_form_table.student_type_id)
            if(extra_fee_table):
                for i in extra_fee_table:
                    extra_fee_discount_table= ExtraFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,extra_fee_structure_id=i.id,status='active')
                    if(extra_fee_discount_table):
                        for k in extra_fee_discount_table:
                            fee_id=k.extra_fee_structure.id
                            fee_name=k.extra_fee_structure.fee_name
                            main_amount=k.main_amount
                            discounted_amount=k.discounted_amount
                            final_amount=k.final_amount
                            total_extra_fee=total_extra_fee+int(final_amount)
                            res['extra_charge'].append({
                                "id":k.extra_fee_structure.id,
                                "fee_name":fee_name,
                                "fee_amount":final_amount
                            })
                    else:        
                        total_extra_fee=total_extra_fee+int(i.fee_amount)
                        res['extra_charge'].append({
                            "id":i.id,
                            "fee_name":i.fee_name,
                            "fee_amount":i.fee_amount
                        })
                res['final_amount']= total_extra_fee+total_amount 
                arr.append(res)

                class_arr=[]
                bus_arr=[]
                extra_fee_arr=[]
                total_amount=[]
                final_arr=[]
                final_amt_arr=[]
                for i in arr:
                    class_arr.append({
                        'id':'',
                        'fee_name':'class_charge',
                        "fee_amount":i['class_charge']
                        })
                    bus_arr.append({
                        'id':'',
                        'fee_name':'bus_root_charge',
                        "fee_amount":i['bus_root_charge'],
                    }) 
                    extra_fee_arr.append(i['extra_charge'])  
                    total_amount.append({'final_amount':i['final_amount']}) 
                 
                final_arr=class_arr+bus_arr+extra_fee_arr[0]
                
                return Response({'res':final_arr,'final_amount':total_amount}) 
            else:
                class_arr=[]
                bus_arr=[]
                final_arr=[]
                total_amounts=[]
                class_arr.append({
                        'id':'',
                        'fee_name':'class_charge',
                        "fee_amount":class_charges
                        })
                bus_arr.append({
                    'id':'',
                    'fee_name':'bus_root_charge',
                    "fee_amount":bus_root_charges,
                }) 
                final_arr=class_arr+bus_arr
                total_amounts.append({'final_amount':total_amount})
                return Response({'res':final_arr,'final_amount':total_amounts}) 
                
class Genrate_Hostel_Fee_api(APIView):
    def get(self, request):
        admission_id = self.request.query_params.get('admission_id')
        month = self.request.query_params.get('month')
        # bus_root_charges=0
        hostel_charge=0
        # class_charges=0
        total_extra_fee=0
        total_amount=0
        arr=[]

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id

        ###########################Hostel Fee#####################
        if(admission_form_table.hostel):
            hostel_fee_discount_table= HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month,status='active')
            if(hostel_fee_discount_table):
                hostel_fee_discount_table1= HostelFeeDiscount.objects.get(admission_id=admission_id,month=month,status='active')
                hostel_charge=float(hostel_fee_discount_table1.final_amount) 
            else:
                hostel_id=admission_form_table.hostel_id
                hostel_table=AddHostel.objects.get(id=hostel_id)
                hostel_charge=float(hostel_table.hostel_fee)/float(hostel_table.hostel_fee_inst)
        
        
        total_amount=hostel_charge
        res= {}
        # res['class_charge']=class_charges
        # res['bus_root_charge']=bus_root_charges
        res['hostel_charge']=hostel_charge
        res['hostel_extra_charge']=[]
        res['final_amount']=''

        hostelextra_fee_table=HostelExtraFeeStructure.objects.filter(month=month,student_type_id=admission_form_table.student_type_id)
        if(hostelextra_fee_table):
            for i in hostelextra_fee_table:
                hostelextra_fee_discount_table= HostelExtraFeeDiscount.objects.filter(admission_id=admission_id,hostel_extra_fee_structure=i.id,month=month,status='active')
                if(hostelextra_fee_discount_table):
                    for k in hostelextra_fee_discount_table:
                        fee_id=k.hostel_extra_fee_structure.id
                        fee_name=k.hostel_extra_fee_structure.fee_name
                        main_amount=k.main_amount
                        discounted_amount=k.discounted_amount
                        final_amount=k.final_amount
                        total_extra_fee=total_extra_fee+int(final_amount)
                        res['hostel_extra_charge'].append({
                            "id":fee_id,
                            "fee_name":fee_name,
                            "fee_amount":final_amount
                        })
                else:        
                    total_extra_fee=total_extra_fee+int(i.fee_amount)
                    res['hostel_extra_charge'].append({
                        "id":i.id,
                        "fee_name":i.fee_name,
                        "fee_amount":i.fee_amount
                    })
            res['final_amount']= total_extra_fee+total_amount 
            arr.append(res)
            return Response(arr) 
        else:
            return Response({
            # "class_charges":class_charges,
            # "bus_root_charges":bus_root_charges,
            "hostel_charge":hostel_charge,
            "final_amount":total_amount
        })        


class Class_Fee_Payment_api(APIView):
    def post(self, request):
        data=request.data
        # amount=data.get('amount')

        admission_id=data.get('admission_id')
        month=data.get('month')
        year=data.get('year')
        fee=data.get('fee')
        
        class_paid_fee=fee[0]['pay_amt']
        bus_paid_fee=fee[1]['pay_amt']
        extra_fee_payment=fee[2:]     

        

        root_fee=0
        class_dues=0
        bus_dues=0
        discounted_class_fee=0
        discounted_bus_fee=0
        class_payable_fee=0
        bus_payable_fee=0
        receipt_ids=0

        extra_fee_total=0
        extra_fee_total_discount=0
        extra_fee_total_payable=0
        paid_extra_fee_total=0

        total_amount=0
        total_discount=0
        total_payble_amount=0
        total_paid_amount=0
        total_dues=0

        receipt_ids1=0
        exists_receipt_id=0
        updated_disc_amt=0
        arr=[]
        extra_fee_amt1=0
        extra_fee_amt2=0

    ############################FOR USE #############################################
        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id
        class_table=AddClass.objects.get(id=class_id)
        class_fee=float(class_table.class_fee)/float(class_table.class_fee_inst)

        if BusRoot.objects.filter(id=admission_form_table.bus_root_id).exists():
            bus_root_table=BusRoot.objects.get(id=admission_form_table.bus_root_id)
            root_fee=float(bus_root_table.root_fee)/float(bus_root_table.root_inst)

        if Receipt.objects.filter(admission_id=admission_id,month=month,year=year).exists():
    ###########################################IF RECIEPT ALREADY GENRATED ##########################################################            
            receipt_table=Receipt.objects.filter(admission_id=admission_id,month=month,year=year).last()
            exists_receipt_id=receipt_table.id
            updated_class_dues=receipt_table.class_dues
            updated_bus_dues=receipt_table.bus_dues

            receipt_create1=Receipt.objects.create(admission_id=admission_id,month=month,year=year)
            receipt_ids1=receipt_create1.id
    ######################################################CLASS FEE###############################################################
            if ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active').exists():
                class_fee_discount_table=ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                discounted_class_fee=class_fee_discount_table.discounted_amount
                class_payable_fee=float(updated_class_dues)-float(class_fee_discount_table.discounted_amount)
                class_dues=float(class_payable_fee)-float(class_paid_fee)
                receipt_update=Receipt.objects.filter(id=receipt_ids1).update(class_fee_discount_id=class_fee_discount_table.id,
                                                admission_id=admission_id,
                                                month=month,
                                                year=year,
                                                class_fee=class_fee,
                                                discounted_class_fee=discounted_class_fee,
                                                class_payable_fee=class_payable_fee,
                                                class_paid_fee=class_paid_fee,
                                                class_dues=class_dues
                                                )
                class_fee_discount_table_udate=ClassFeeDiscount.objects.filter(id=class_fee_discount_table.id).update(status='in-active')                                
            else:
                class_payable_fee=float(updated_class_dues)
                class_dues=float(updated_class_dues)-float(class_paid_fee)
                receipt_create=Receipt.objects.filter(id=receipt_ids1).update(admission_id=admission_id,
                                                month=month,
                                                year=year,
                                                class_fee=class_fee,
                                                discounted_class_fee=0,
                                                class_payable_fee=class_payable_fee,
                                                class_paid_fee=class_paid_fee,
                                                class_dues=class_dues)
    #################################################BUS FEE###############################################################
            if BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active').exists():
                bus_fee_discount_table=BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                discounted_bus_fee=bus_fee_discount_table.discounted_amount
                bus_payable_fee=float(updated_bus_dues)-float(bus_fee_discount_table.discounted_amount)
                bus_dues=float(bus_payable_fee)-float(bus_paid_fee)
                receipt_create=Receipt.objects.filter(id=receipt_ids1).update(bus_fee_discount_id=bus_fee_discount_table.id,
                                            admission_id=admission_id,
                                            month=month,year=year,
                                            bus_fee=root_fee,
                                            discounted_bus_fee=discounted_bus_fee,
                                            bus_payable_fee=bus_payable_fee,
                                            bus_paid_fee=bus_paid_fee,
                                            bus_dues=bus_dues
                                            ) 
                bus_fee_discount_table_update=BusFeeDiscount.objects.filter(id=bus_fee_discount_table.id).update(status='in-active')                                                   
            else:
                bus_payable_fee=float(updated_bus_dues)
                bus_dues=float(updated_bus_dues)-float(bus_paid_fee)
                receipt_create=Receipt.objects.filter(id=receipt_ids1).update(
                                                        bus_fee=root_fee,
                                                        discounted_bus_fee=0,
                                                        bus_payable_fee=bus_payable_fee,
                                                        bus_paid_fee=bus_paid_fee,
                                                        bus_dues=bus_dues)  
    #################################################EXTRA  FEE###############################################################
            if ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month,year=year):
                extra_fee_structure_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month,year=year)
                for i in extra_fee_structure_table:
                    extra_fee_total=float(extra_fee_total)+float(i.fee_amount)
                    if ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,year=year,status='active'):
                        extra_fee_discount_table=ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,year=year,status='active')
                        for j in extra_fee_discount_table:
                            extra_fee_total_discount=float(extra_fee_total_discount)+float(j.discounted_amount)
                            # extra_fee_total_payable=float(extra_fee_total_payable)+float(j.final_amount)
                            # updated_disc_amt=j.discounted_amount
                            # arr.append(j.extra_fee_structure.fee_name)

                            extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids1,
                            extra_fee_structure_id=j.extra_fee_structure_id,
                            extra_fee_name=j.extra_fee_structure.fee_name,
                            extra_fee=j.main_amount,
                            discounted_extra_fee=j.discounted_amount,
                            # payable_extra_fee=j.final_amount,
                            )
                            extra_fee_discount_table_update=ExtraFeeDiscount.objects.filter(id=j.id).update(status='in-active')    
                    
                    else:
                        updated_disc_amt=0
                        # extra_fee_total_payable=float(extra_fee_total_payable)+float(i.fee_amount)
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids1,
                            extra_fee_structure_id=i.id,
                            extra_fee_name=i.fee_name,
                            extra_fee=i.fee_amount,
                            discounted_extra_fee=updated_disc_amt,
                            # payable_extra_fee=i.fee_amount,
                            )
            if extra_fee_payment:            
                for k in extra_fee_payment:
                    id=  k['id'] 
                    
                    if Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt_id,extra_fee_structure_id=id).exists():
                        extra_fee_receipt_table=Receipt_for_ExtraFee.objects.get(receipt_id=exists_receipt_id,extra_fee_structure_id=id)
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.get(receipt_id=receipt_ids1,extra_fee_structure_id=id)
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.filter(receipt_id=receipt_ids1,extra_fee_structure_id=id).update(
                                        # payable_extra_fee=(float(extra_fee_receipt_table.payable_extra_fee)-float(extra_fee_receipt.discounted_extra_fee))-float(k['paid_amount']),
                                        payable_extra_fee=(float(extra_fee_receipt_table.extra_fee_dues)-float(extra_fee_receipt.discounted_extra_fee)),

                                        ) 
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.get(receipt_id=receipt_ids1,extra_fee_structure_id=id)
                        extra_fee_amt1=float(extra_fee_amt1)+float(extra_fee_receipt.payable_extra_fee)
                                      
                    else:
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.get(receipt_id=receipt_ids1,extra_fee_structure_id=id)
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.filter(receipt_id=receipt_ids1,extra_fee_structure_id=id).update(
                                        payable_extra_fee=float(extra_fee_receipt.extra_fee)-float(extra_fee_receipt.discounted_extra_fee),
                                        extra_fee_dues=(float(extra_fee_receipt_table.extra_fee)-float(extra_fee_receipt.discounted_extra_fee))-float(k['pay_amt'])

                        )
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.get(receipt_id=receipt_ids1,extra_fee_structure_id=id)
                        extra_fee_amt2=float(extra_fee_amt2)+float(extra_fee_receipt.payable_extra_fee)


           

            if extra_fee_payment: 
                for k in extra_fee_payment:
                    paid_extra_fee_total=float(paid_extra_fee_total)+float(k['pay_amt']) 
                    extra_fee_receipt_update=Receipt_for_ExtraFee.objects.filter(receipt_id=receipt_ids1,extra_fee_structure_id=k['id'])
                    for j in extra_fee_receipt_update:
                        extra_fee_receipt_update1=Receipt_for_ExtraFee.objects.filter(id=j.id)
                        extra_fee_receipt_update1=Receipt_for_ExtraFee.objects.filter(id=j.id).update(
                            paid_extra_fee=k['pay_amt'],
                            extra_fee_dues=float(j.payable_extra_fee)-float(k['pay_amt'])
                        )
                        extra_fee_receipt_update1=Receipt_for_ExtraFee.objects.get(id=j.id)
                        extra_fee_total_payable=float(extra_fee_total_payable)+float(extra_fee_receipt_update1.extra_fee_dues)

            to_get_previsous_bill_paid_data=Receipt.objects.get(id=exists_receipt_id)
            total_amount=float(class_fee)+float(root_fee)+float(extra_fee_total)
            total_discount=float(discounted_class_fee)+float(discounted_bus_fee)+float(extra_fee_total_discount)
            total_paid_amount=float(class_paid_fee)+float(bus_paid_fee)+float(paid_extra_fee_total)
            print(extra_fee_amt1+extra_fee_amt2,'extra_fee_amt1+extra_fee_amt2')
            updated_payble_amount=extra_fee_amt1+extra_fee_amt2
            total_payble_amount=float(class_payable_fee)+float(bus_payable_fee)+float(updated_payble_amount)
            total_dues=float(total_payble_amount)-float(total_paid_amount)
            receipt_create=Receipt.objects.filter(id=receipt_ids1).update(
                                                        total_amount=total_amount,
                                                        total_discounted_amount=total_discount,
                                                        total_payble_amount=total_payble_amount,
                                                        previous_bill_current_month_paid_amount=to_get_previsous_bill_paid_data.paid_amount,
                                                        paid_amount=total_paid_amount,
                                                        total_dues=total_dues)
                
            return Response({'messages':"Receipt again genrated!!!",'status':status.HTTP_201_CREATED})
        else:
            receipt_create=Receipt.objects.create(admission_id=admission_id,month=month,year=year)
            receipt_ids=receipt_create.id
    ###########################################FIRST TIME PAYMENT ##########################################################            
    #########################################CLASS FEE ##############################################################
            if ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,status='active').exists():
                class_fee_discount_table=ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,status='active')
                discounted_class_fee=class_fee_discount_table.discounted_amount
                class_payable_fee=float(class_fee)-float(class_fee_discount_table.discounted_amount)
                class_dues=float(class_payable_fee)-float(class_paid_fee)
                receipt_update=Receipt.objects.filter(id=receipt_ids).update(class_fee_discount_id=class_fee_discount_table.id,
                                                admission_id=admission_id,
                                                month=month,
                                                class_fee=class_fee,
                                                discounted_class_fee=discounted_class_fee,
                                                class_payable_fee=class_payable_fee,
                                                class_paid_fee=class_paid_fee,
                                                class_dues=class_dues
                                                )
                class_fee_discount_table_update=ClassFeeDiscount.objects.filter(id=class_fee_discount_table.id).update(status='in-active')                                
            else:
                class_dues=float(class_fee)-float(class_paid_fee)
                class_payable_fee=float(class_fee)
                receipt_create=Receipt.objects.filter(id=receipt_ids).update(admission_id=admission_id,
                                                month=month,
                                                class_fee=class_fee,
                                                discounted_class_fee=0,
                                                class_payable_fee=class_payable_fee,
                                                class_paid_fee=class_paid_fee,
                                                class_dues=class_dues)
    #########################################BUS FEE ##############################################################   
            if BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,status='active').exists():
                bus_fee_discount_table=BusFeeDiscount.objects.get(admission_id=admission_id,month=month,status='active')
                discounted_bus_fee=bus_fee_discount_table.discounted_amount
                bus_payable_fee=float(root_fee)-float(bus_fee_discount_table.discounted_amount)
                bus_dues=float(bus_payable_fee)-float(bus_paid_fee)
                receipt_create=Receipt.objects.filter(id=receipt_ids).update(bus_fee_discount_id=bus_fee_discount_table.id,
                                            admission_id=admission_id,
                                            month=month,
                                            bus_fee=root_fee,
                                            discounted_bus_fee=discounted_bus_fee,
                                            bus_payable_fee=bus_payable_fee,
                                            bus_paid_fee=bus_paid_fee,
                                            bus_dues=bus_dues
                                            )  

                bus_fee_discount_table_update=BusFeeDiscount.objects.filter(id=bus_fee_discount_table.id).update(status='in-active')                            
            else:
                bus_payable_fee=float(root_fee)
                bus_dues=float(root_fee)-float(bus_paid_fee)
                receipt_create=Receipt.objects.filter(id=receipt_ids).update(
                                                        bus_fee=root_fee,
                                                        discounted_bus_fee=0,
                                                        bus_payable_fee=bus_payable_fee,
                                                        bus_paid_fee=bus_paid_fee,
                                                        bus_dues=bus_dues) 

    #########################################Extra FEE ##############################################################                                        
            if ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month):
                extra_fee_structure_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month)
                for i in extra_fee_structure_table:
                    extra_fee_total=float(extra_fee_total)+float(i.fee_amount)
                    if ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,status='active'):
                        extra_fee_discount_table=ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,status='active')
                        for j in extra_fee_discount_table:
                            extra_fee_total_discount=float(extra_fee_total_discount)+float(j.discounted_amount)
                            extra_fee_total_payable=float(extra_fee_total_payable)+float(j.final_amount)
                            extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids,
                            extra_fee_structure_id=j.extra_fee_structure_id,
                            extra_fee_name=j.extra_fee_structure.fee_name,
                            extra_fee=j.main_amount,
                            discounted_extra_fee=j.discounted_amount,
                            payable_extra_fee=j.final_amount,
                            )
                            extra_fee_discount_table_update=ExtraFeeDiscount.objects.filter(id=j.id).update(status='in-active')    
                       

                    else:
                        extra_fee_total_payable=float(extra_fee_total_payable)+float(i.fee_amount)
                        extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids,
                            extra_fee_structure_id=i.id,
                            extra_fee_name=i.fee_name,
                            extra_fee=i.fee_amount,
                            discounted_extra_fee=0,
                            payable_extra_fee=i.fee_amount,
                            )
                        
        if extra_fee_payment: 
            for k in extra_fee_payment:
                paid_extra_fee_total=float(paid_extra_fee_total)+float(k['pay_amt']) 
                extra_fee_receipt_update=Receipt_for_ExtraFee.objects.filter(receipt_id=receipt_ids,extra_fee_structure_id=k['id'])
                for j in extra_fee_receipt_update:
                    extra_fee_receipt_update1=Receipt_for_ExtraFee.objects.filter(id=j.id).update(
                        paid_extra_fee=k['pay_amt'],
                        extra_fee_dues=float(j.payable_extra_fee)-float(k['pay_amt'])
                    )                
       
                                                                                                                                         
        total_amount=float(class_fee)+float(root_fee)+float(extra_fee_total)
        total_discount=float(discounted_class_fee)+float(discounted_bus_fee)+float(extra_fee_total_discount)
        total_payble_amount=float(class_payable_fee)+float(bus_payable_fee)+float(extra_fee_total_payable)
        total_paid_amount=float(class_paid_fee)+float(bus_paid_fee)+float(paid_extra_fee_total)
        total_dues=total_payble_amount-total_paid_amount
        receipt_create=Receipt.objects.filter(id=receipt_ids).update(
                                                        total_amount=total_amount,
                                                        total_discounted_amount=total_discount,
                                                        total_payble_amount=total_payble_amount,
                                                        paid_amount=total_paid_amount,
                                                        total_dues=total_dues)

                                                                                                  
        return Response({'messages':"Receipt genrated successfully!!!",'status':status.HTTP_201_CREATED})                                
                                        

class Hostel_Fee_Payment_api(APIView):
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        month=data.get('month')
        hostel_paid_fee=data.get('hostel_paid_fee')
        extra_hostel_payment=data.get('extra_hostel_payment')
        
        hostel_fee=0
        hostel_dues=0
        discounted_hostel_fee=0
        hostel_payable_fee=0
        receipt_ids=0

        extra_fee_total=0
        extra_fee_total_discount=0
        extra_fee_total_payable=0
        paid_extra_fee_total=0

        total_amount=0
        total_discount=0
        total_payble_amount=0
        total_paid_amount=0
        total_dues=0

        receipt_ids1=0
        exists_receipt_id=0
        updated_disc_amt=0
        arr=[]

    ############################FOR USE #############################################
        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id
        class_table=AddClass.objects.get(id=class_id)
        # class_fee=float(class_table.class_fee)/float(class_table.class_fee_inst)

        if AddHostel.objects.filter(id=admission_form_table.hostel_id).exists():
            hostel_table=AddHostel.objects.get(id=admission_form_table.hostel_id)
            hostel_fee=float(hostel_table.hostel_fee)/float(hostel_table.hostel_fee_inst)

        if Hostel_Receipt.objects.filter(admission_id=admission_id,month=month).exists():
    ###########################################IF RECIEPT ALREADY GENRATED ##########################################################            
            return Response({'messages':"Hostel Receipt again genrated!!!",'status':status.HTTP_201_CREATED})
        else:
            receipt_create=Hostel_Receipt.objects.create(admission_id=admission_id,month=month)
            receipt_ids=receipt_create.id
    ###########################################FIRST TIME PAYMENT ##########################################################            
    
    #########################################HOSTEL FEE ##############################################################   
            if HostelFeeDiscount.objects.filter(admission_id=admission_id,month=month,status='active').exists():
                hostel_fee_discount_table=HostelFeeDiscount.objects.get(admission_id=admission_id,month=month,status='active')
                discounted_hostel_fee=hostel_fee_discount_table.discounted_amount
                hostel_payable_fee=float(hostel_fee)-float(hostel_fee_discount_table.discounted_amount)
                hostel_dues=float(hostel_payable_fee)-float(hostel_paid_fee)
                receipt_create=Hostel_Receipt.objects.filter(id=receipt_ids).update(hostel_fee_discount_id=hostel_fee_discount_table.id,
                                            admission_id=admission_id,
                                            month=month,
                                            hostel_fee=hostel_fee,
                                            discounted_hostel_fee=discounted_hostel_fee,
                                            hostel_payable_fee=hostel_payable_fee,
                                            hostel_paid_fee=hostel_paid_fee,
                                            hostel_dues=hostel_dues
                                            )  

                hostel_fee_discount_table_update=HostelFeeDiscount.objects.filter(id=hostel_fee_discount_table.id).update(status='in-active')                            
            else:
                hostel_payable_fee=float(hostel_fee)
                hostel_dues=float(hostel_fee)-float(hostel_paid_fee)
                receipt_create=Hostel_Receipt.objects.filter(id=receipt_ids).update(
                                                        hostel_fee=hostel_fee,
                                                        discounted_hostel_fee=0,
                                                        hostel_payable_fee=hostel_payable_fee,
                                                        hostel_paid_fee=hostel_paid_fee,
                                                        hostel_dues=hostel_dues) 

    #########################################Extra FEE ##############################################################                                        
        #     if ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month):
        #         extra_fee_structure_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month)
        #         for i in extra_fee_structure_table:
        #             extra_fee_total=float(extra_fee_total)+float(i.fee_amount)
        #             if ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,status='active'):
        #                 extra_fee_discount_table=ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,status='active')
        #                 for j in extra_fee_discount_table:
        #                     extra_fee_total_discount=float(extra_fee_total_discount)+float(j.discounted_amount)
        #                     extra_fee_total_payable=float(extra_fee_total_payable)+float(j.final_amount)
        #                     extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids,
        #                     extra_fee_structure_id=j.extra_fee_structure_id,
        #                     extra_fee_name=j.extra_fee_structure.fee_name,
        #                     extra_fee=j.main_amount,
        #                     discounted_extra_fee=j.discounted_amount,
        #                     payable_extra_fee=j.final_amount,
        #                     )
        #                     extra_fee_discount_table_update=ExtraFeeDiscount.objects.filter(id=j.id).update(status='in-active')    
                       

        #             else:
        #                 extra_fee_total_payable=float(extra_fee_total_payable)+float(i.fee_amount)
        #                 extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids,
        #                     extra_fee_structure_id=i.id,
        #                     extra_fee_name=i.fee_name,
        #                     extra_fee=i.fee_amount,
        #                     discounted_extra_fee=0,
        #                     payable_extra_fee=i.fee_amount,
        #                     )
                        
        # if extra_fee_payment: 
        #     for k in extra_fee_payment:
        #         paid_extra_fee_total=float(paid_extra_fee_total)+float(k['paid_amount']) 
        #         extra_fee_receipt_update=Receipt_for_ExtraFee.objects.filter(receipt_id=receipt_ids,extra_fee_structure_id=k['extra_fee_id'])
        #         for j in extra_fee_receipt_update:
        #             extra_fee_receipt_update1=Receipt_for_ExtraFee.objects.filter(id=j.id).update(
        #                 paid_extra_fee=k['paid_amount'],
        #                 extra_fee_dues=float(j.payable_extra_fee)-float(k['paid_amount'])
        #             )                
       
                                                                                                                                         
        # total_amount=float(class_fee)+float(root_fee)+float(extra_fee_total)
        # total_discount=float(discounted_class_fee)+float(discounted_bus_fee)+float(extra_fee_total_discount)
        # total_payble_amount=float(class_payable_fee)+float(bus_payable_fee)+float(extra_fee_total_payable)
        # total_paid_amount=float(class_paid_fee)+float(bus_paid_fee)+float(paid_extra_fee_total)
        # total_dues=total_payble_amount-total_paid_amount
        # receipt_create=Receipt.objects.filter(id=receipt_ids).update(
        #                                                 total_amount=total_amount,
        #                                                 total_discounted_amount=total_discount,
        #                                                 total_payble_amount=total_payble_amount,
        #                                                 paid_amount=total_paid_amount,
        #                                                 total_dues=total_dues)

                                                                                                  
        return Response({'messages':"Receipt genrated successfully!!!",'status':status.HTTP_201_CREATED})                                


######################################### NEW WORK FOR API INTEGRSTIONS#################################
class PayFee_student_details(APIView):
    def get(self, request):
        admission_id = self.request.query_params.get('admission_id')
        arr=[]
        admissions_details = Admissions_form.objects.filter(id=admission_id)
        for i in admissions_details:
            arr.append({
                'id':i.id,
                "student_name":i.reception.student_name,
                "class_name":i.reception.class_name.class_name,
                "father_name":i.reception.father_name,
                "mother_name":i.reception.mother_name,
                'admission_no':i.admission_no,
                'roll_no':i.roll_no,
                "section_name":i.section.section_name,
            })
        return Response(arr)  

class Month_wise_total_fee_api(APIView):
    def post(self, request):
        data=request.data
        admission_id =data.get('admission_id')
        year = data.get('year')
        bus_root_charges=0
        class_charges=0
        total_extra_fee=0
        total_amount=0
        arr=[]
        class_dues=0
        bus_dues=0

        final_amount=0

        admission_form_table=Admissions_form.objects.get(id=admission_id)
        reception_table=Reception.objects.get(id=admission_form_table.reception_id)
        class_id=reception_table.class_name_id
        for i in data['month']:
            month=i
            if Receipt.objects.filter(admission_id=admission_id,month=month,year=year,).exists():
                exists_receipt=Receipt.objects.filter(admission_id=admission_id,month=month,year=year).last()
                class_dues=exists_receipt.class_dues
                bus_dues=exists_receipt.bus_dues
        #####################################BUS DUES####################################################################
                if(admission_form_table.bus_root):
                    bus_fee_discount_table= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
                    if(bus_fee_discount_table):
                        bus_fee_discount_table1= BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                        discounted_amount=float(bus_fee_discount_table1.discounted_amount)
                        bus_dues=float(bus_dues)-float(discounted_amount) 
        ########################################CLASS DUES####################################################################
                class_fee_discount_table= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
                if(class_fee_discount_table):
                    class_fee_discount_table1= ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    discounted_amount=float(class_fee_discount_table1.discounted_amount)
                    class_dues=float(class_dues)-float(discounted_amount) 

        #############################################Extra Fee##################################################################
                total_amount=float(class_dues)+float(bus_dues)
                
                if Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt).exists():
                    extra_fee_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,month=month,year=year,student_type_id=admission_form_table.student_type_id)
                    if(extra_fee_table):
                        for i in extra_fee_table:
                            extra_fee_discount_table= ExtraFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,extra_fee_structure_id=i.id,status='active')
                            if(extra_fee_discount_table):
                                for k in extra_fee_discount_table:
                                    fee_id=k.extra_fee_structure.id
                                    discounted_amount=k.discounted_amount
                                    final_amount=k.final_amount
                                    receipt_for_extrafee_exits_table=Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt,extra_fee_structure_id=fee_id)
                                    if receipt_for_extrafee_exits_table:
                                        receipt_for_extrafee_exits_table1=Receipt_for_ExtraFee.objects.get(receipt_id=exists_receipt,extra_fee_structure_id=fee_id)
                                        extra_fee_dues=receipt_for_extrafee_exits_table1.extra_fee_dues
                                        total_extra_fee=total_extra_fee+(float(extra_fee_dues)-float(discounted_amount))
                                        
                                    else:    
                                        final_amount=k.final_amount
                                        total_extra_fee=total_extra_fee+int(final_amount)
                            else:
                                receipt_for_extrafee_exits_table=Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt,extra_fee_structure_id=i.id)
                                if receipt_for_extrafee_exits_table:
                                    for l in receipt_for_extrafee_exits_table:
                                        if l.extra_fee_name == i.fee_name:
                                            print(l.extra_fee_dues,'elssssssssss')    
                                            total_extra_fee=total_extra_fee+float(l.extra_fee_dues)
                                else:
                                    total_extra_fee=total_extra_fee+float(i.fee_amount)
                        final_amount= total_extra_fee+total_amount 
                    
                    else:  
                        receipt_for_extrafee_exits_table=Receipt_for_ExtraFee.objects.filter(receipt_id=exists_receipt)
                        for l in receipt_for_extrafee_exits_table:
                            total_extra_fee=total_extra_fee+float(l.extra_fee_dues)

                        final_amount=float(total_extra_fee)+float(total_amount) 
                       
                else:    
                    extra_fee_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,month=month,year=year,student_type_id=admission_form_table.student_type_id)
                    if(extra_fee_table):
                        for i in extra_fee_table:
                            extra_fee_discount_table= ExtraFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,extra_fee_structure_id=i.id,status='active')
                            if(extra_fee_discount_table):
                                for k in extra_fee_discount_table:
                                    fee_id=k.extra_fee_structure.id
                                    fee_name=k.extra_fee_structure.fee_name
                                    main_amount=k.main_amount
                                    discounted_amount=k.discounted_amount
                                    final_amount=k.final_amount
                                    total_extra_fee=total_extra_fee+int(final_amount)
                            else:    
                                total_extra_fee=total_extra_fee+int(i.fee_amount)
                            final_amount= total_extra_fee +total_amount
                final_amount=final_amount
                print(final_amount,'fff')

            else:
                ###########################bus Fee#####################
                if(admission_form_table.bus_root):
                    bus_fee_discount_table= BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
                    if(bus_fee_discount_table):
                        bus_fee_discount_table1= BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                        bus_root_charges=float(bus_fee_discount_table1.final_amount) 
                    else:
                        bus_root_id=admission_form_table.bus_root_id
                        bus_root_table=BusRoot.objects.get(id=bus_root_id)
                        bus_root_charges=float(bus_root_table.root_fee)/float(bus_root_table.root_inst)
            
                ##################class Fee####################
                class_fee_discount_table= ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active')
                if(class_fee_discount_table):
                    class_fee_discount_table1= ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    class_charges=float(class_fee_discount_table1.final_amount) 
                else:
                    class_table=AddClass.objects.get(id=class_id)
                    class_charges=float(class_table.class_fee)/float(class_table.class_fee_inst)

                ##################Extra Fee####################
                
                total_amount=total_amount+class_charges+bus_root_charges
                extra_fee_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,month=month,year=year,student_type_id=admission_form_table.student_type_id)
                if(extra_fee_table):
                    for i in extra_fee_table:
                        extra_fee_discount_table= ExtraFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,extra_fee_structure_id=i.id,status='active')
                        if(extra_fee_discount_table):
                            for k in extra_fee_discount_table:
                                fee_id=k.extra_fee_structure.id
                                fee_name=k.extra_fee_structure.fee_name
                                main_amount=k.main_amount
                                discounted_amount=k.discounted_amount
                                total_extra_fee=total_extra_fee+int(k.final_amount)
                        else:        
                            total_extra_fee=total_extra_fee+int(i.fee_amount)
                    final_amount= total_extra_fee+total_amount                      
                else:
                    
                    final_amount=final_amount +class_charges+bus_root_charges 
        return Response({'final_amount':final_amount})    
            

###############################################################One Time Class Payment################################################################
class One_time_class_fee_payment_api(APIView):
    def post(self, request):
        data=request.data
        admission_id=data.get('admission_id')
        paid_amount=data.get('paid_amount')
        year=data.get('year')
        root_fee=0
        class_dues=0
        bus_dues=0
        discounted_class_fee=0
        discounted_bus_fee=0
        class_payable_fee=0
        bus_payable_fee=0
        receipt_ids=0

        extra_fee_total=0
        extra_fee_total_discount=0
        extra_fee_total_payable=0
        paid_extra_fee_total=0

        total_amount=0
        total_discount=0
        total_payble_amount=0
        total_paid_amount=0
        total_dues=0

        receipt_ids1=0
        exists_receipt_id=0
        updated_disc_amt=0
        arr=[]
        print(admission_id,paid_amount)
        for i in data['month']:
            month=i
            print(i,'iiiii')
        ############################FOR USE #############################################
            admission_form_table=Admissions_form.objects.get(id=admission_id)
            reception_table=Reception.objects.get(id=admission_form_table.reception_id)
            class_id=reception_table.class_name_id
            class_table=AddClass.objects.get(id=class_id)
            class_fee=float(class_table.class_fee)/float(class_table.class_fee_inst)

            if BusRoot.objects.filter(id=admission_form_table.bus_root_id).exists():
                bus_root_table=BusRoot.objects.get(id=admission_form_table.bus_root_id)
                root_fee=float(bus_root_table.root_fee)/float(bus_root_table.root_inst)
            
            if Receipt.objects.filter(admission_id=admission_id,month=month,year=year).exists():
        ###########################################IF RECIEPT ALREADY GENRATED ##########################################################  
                receipt_table=Receipt.objects.filter(admission_id=admission_id,month=month,year=year).last()
                exists_receipt_id=receipt_table.id
                updated_class_dues=receipt_table.class_dues
                updated_bus_dues=receipt_table.bus_dues

                receipt_create1=Receipt.objects.create(admission_id=admission_id,month=month,year=year)
                receipt_ids1=receipt_create1.id
        ######################################################CLASS FEE###############################################################
                if ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active').exists():
                    class_fee_discount_table=ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    discounted_class_fee=class_fee_discount_table.discounted_amount
                    class_payable_fee=float(updated_class_dues)-float(class_fee_discount_table.discounted_amount)
                    class_dues=float(class_payable_fee)-float(class_paid_fee)
                    receipt_update=Receipt.objects.filter(id=receipt_ids1).update(class_fee_discount_id=class_fee_discount_table.id,
                                                    admission_id=admission_id,
                                                    class_fee=class_fee,
                                                    discounted_class_fee=discounted_class_fee,
                                                    class_payable_fee=class_payable_fee,
                                                    class_paid_fee=class_payable_fee,#Because customer is paying whole amount at a time
                                                    class_dues=0
                                                    )
                    class_fee_discount_table_udate=ClassFeeDiscount.objects.filter(id=class_fee_discount_table.id).update(status='in-active')                                
                else:
                    class_payable_fee=float(updated_class_dues)
                    class_dues=float(updated_class_dues)-float(class_paid_fee)
                    receipt_create=Receipt.objects.filter(id=receipt_ids1).update(admission_id=admission_id,
                                                    class_fee=class_fee,
                                                    discounted_class_fee=0,
                                                    class_payable_fee=class_payable_fee,
                                                    class_paid_fee=class_payable_fee,#Because customer is paying whole amount at a time
                                                    class_dues=0
                                                    )
        #################################################BUS FEE###############################################################
                if BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active').exists():
                    bus_fee_discount_table=BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    discounted_bus_fee=bus_fee_discount_table.discounted_amount
                    bus_payable_fee=float(updated_bus_dues)-float(bus_fee_discount_table.discounted_amount)
                    bus_dues=float(bus_payable_fee)-float(bus_paid_fee)
                    receipt_create=Receipt.objects.filter(id=receipt_ids1).update(bus_fee_discount_id=bus_fee_discount_table.id,
                                                admission_id=admission_id,
                                                bus_fee=root_fee,
                                                discounted_bus_fee=discounted_bus_fee,
                                                bus_payable_fee=bus_payable_fee,
                                                bus_paid_fee=bus_payable_fee,#Because customer is paying whole amount at a time
                                                bus_dues=0
                                                ) 
                    bus_fee_discount_table_update=BusFeeDiscount.objects.filter(id=bus_fee_discount_table.id).update(status='in-active')                                                   
                else:
                    bus_payable_fee=float(updated_bus_dues)
                    bus_dues=float(updated_bus_dues)-float(bus_paid_fee)
                    receipt_create=Receipt.objects.filter(id=receipt_ids1).update(
                                                            bus_fee=root_fee,
                                                            discounted_bus_fee=0,
                                                            bus_payable_fee=bus_payable_fee,
                                                            bus_paid_fee=bus_payable_fee,#Because customer is paying whole amount at a time
                                                            bus_dues=0)  

#################################################EXTRA  FEE###############################################################
                if ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month,year=year):
                    extra_fee_structure_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month,year=year)
                    for i in extra_fee_structure_table:
                        extra_fee_total=float(extra_fee_total)+float(i.fee_amount)
                        if ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,year=year,status='active'):
                            extra_fee_discount_table=ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,year=year,status='active')
                            for j in extra_fee_discount_table:
                                extra_fee_total_discount=float(extra_fee_total_discount)+float(j.discounted_amount)
                                extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids1,
                                extra_fee_structure_id=j.extra_fee_structure_id,
                                extra_fee_name=j.extra_fee_structure.fee_name,
                                extra_fee=j.main_amount,
                                discounted_extra_fee=j.discounted_amount,
                                )
                                extra_fee_discount_table_update=ExtraFeeDiscount.objects.filter(id=j.id).update(status='in-active')    
                        
                        else:
                            updated_disc_amt=0
                            extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids1,
                                extra_fee_structure_id=i.id,
                                extra_fee_name=i.fee_name,
                                extra_fee=i.fee_amount,
                                discounted_extra_fee=updated_disc_amt,
                                )                                                                              
                return Response('already genrated')   
            else:
        ###########################################FIRST TIME PAYMENT ##########################################################            
                receipt_create=Receipt.objects.create(admission_id=admission_id,month=month,year=year)
                receipt_ids=receipt_create.id
        #########################################CLASS FEE ##############################################################
                if ClassFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active').exists():
                    class_fee_discount_table=ClassFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    discounted_class_fee=class_fee_discount_table.discounted_amount
                    class_payable_fee=float(class_fee)-float(class_fee_discount_table.discounted_amount)
                    # class_dues=float(class_payable_fee)-float(class_paid_fee)
                    receipt_update=Receipt.objects.filter(id=receipt_ids).update(class_fee_discount_id=class_fee_discount_table.id,
                                                    admission_id=admission_id,
                                                    class_fee=class_fee,
                                                    discounted_class_fee=discounted_class_fee,
                                                    class_payable_fee=class_payable_fee,
                                                    class_paid_fee=class_payable_fee, #Because customer is paying whole amount at a time 
                                                    class_dues=0
                                                    )
                    class_fee_discount_table_update=ClassFeeDiscount.objects.filter(id=class_fee_discount_table.id).update(status='in-active')                                
                else:
                    # class_dues=float(class_fee)-float(class_paid_fee)
                    class_payable_fee=float(class_fee)
                    receipt_create=Receipt.objects.filter(id=receipt_ids).update(admission_id=admission_id,
                                                    class_fee=class_fee,
                                                    discounted_class_fee=0,
                                                    class_payable_fee=class_payable_fee,
                                                    class_paid_fee=class_payable_fee,#Because customer is paying whole amount at a time
                                                    class_dues=0
                                                    )
    #########################################BUS FEE ##############################################################   
                if BusFeeDiscount.objects.filter(admission_id=admission_id,month=month,year=year,status='active').exists():
                    bus_fee_discount_table=BusFeeDiscount.objects.get(admission_id=admission_id,month=month,year=year,status='active')
                    discounted_bus_fee=bus_fee_discount_table.discounted_amount
                    bus_payable_fee=float(root_fee)-float(bus_fee_discount_table.discounted_amount)
                    # bus_dues=float(bus_payable_fee)-float(bus_paid_fee)
                    receipt_create=Receipt.objects.filter(id=receipt_ids).update(bus_fee_discount_id=bus_fee_discount_table.id,
                                                admission_id=admission_id,
                                                bus_fee=root_fee,
                                                discounted_bus_fee=discounted_bus_fee,
                                                bus_payable_fee=bus_payable_fee,
                                                bus_paid_fee=bus_payable_fee,#Because customer is paying whole amount at a time 
                                                bus_dues=0
                                                )  

                    bus_fee_discount_table_update=BusFeeDiscount.objects.filter(id=bus_fee_discount_table.id).update(status='in-active')                            
                else:
                    bus_payable_fee=float(root_fee)
                    # bus_dues=float(root_fee)-float(bus_paid_fee)
                    receipt_create=Receipt.objects.filter(id=receipt_ids).update(
                                                            bus_fee=root_fee,
                                                            discounted_bus_fee=0,
                                                            bus_payable_fee=bus_payable_fee,
                                                            bus_paid_fee=bus_payable_fee,#Because customer is paying whole amount at a time 
                                                            bus_dues=0) 
   ##################################################EXTRA FEE########################################################################3                                                     

                if ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month,year=year):
                    extra_fee_structure_table=ExtraFeeStructure.objects.filter(class_name_id=class_id,student_type_id=admission_form_table.student_type_id,month=month,year=year)
                    for i in extra_fee_structure_table:
                        extra_fee_total=float(extra_fee_total)+float(i.fee_amount)
                        if ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,year=year,status='active'):
                            extra_fee_discount_table=ExtraFeeDiscount.objects.filter(admission_id=admission_id,extra_fee_structure_id=i.id,month=month,year=year,status='active')
                            for j in extra_fee_discount_table:
                                extra_fee_total_discount=float(extra_fee_total_discount)+float(j.discounted_amount)
                                extra_fee_total_payable=float(extra_fee_total_payable)+float(j.final_amount)
                                extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids,
                                extra_fee_structure_id=j.extra_fee_structure_id,
                                extra_fee_name=j.extra_fee_structure.fee_name,
                                extra_fee=j.main_amount,
                                discounted_extra_fee=j.discounted_amount,
                                payable_extra_fee=j.final_amount,
                                paid_extra_fee=j.final_amount,#Because customer is paying whole amount at a time 
                                extra_fee_dues=0
                                )
                                extra_fee_discount_table_update=ExtraFeeDiscount.objects.filter(id=j.id).update(status='in-active')    
                        

                        else:
                            extra_fee_total_payable=float(extra_fee_total_payable)+float(i.fee_amount)
                            extra_fee_receipt=Receipt_for_ExtraFee.objects.create(receipt_id=receipt_ids,
                                extra_fee_structure_id=i.id,
                                extra_fee_name=i.fee_name,
                                extra_fee=i.fee_amount,
                                discounted_extra_fee=0,
                                payable_extra_fee=i.fee_amount,
                                paid_extra_fee=i.fee_amount,#Because customer is paying whole amount at a time 
                                extra_fee_dues=0
                                ) 

                total_amount=float(class_fee)+float(root_fee)+float(extra_fee_total)
                total_discount=float(discounted_class_fee)+float(discounted_bus_fee)+float(extra_fee_total_discount)
                total_payble_amount=float(class_payable_fee)+float(bus_payable_fee)+float(extra_fee_total_payable)
                receipt_create=Receipt.objects.filter(id=receipt_ids).update(
                                                        total_amount=total_amount,
                                                        total_discounted_amount=total_discount,
                                                        total_payble_amount=total_payble_amount,
                                                        paid_amount=total_payble_amount,#Because customer is paying whole amount at a time 
                                                        total_dues=0)


        return Response({'messages':"Receipt genrated successfully!!!",'status':status.HTTP_201_CREATED}) 
        
class Dashboard_api(APIView):
    def get(self, request):
        active_student_count=0
        active_bus_student_count=0
        active_hostel_student_count=0
        active_staff_count=0
        arr=[]

        active_students=Admissions_form.objects.filter(is_active=True)
        for i in active_students:
            active_student_count=active_student_count+1
            active_bus_student_count=active_bus_student_count+1
            active_hostel_student_count=active_hostel_student_count+1
        active_staffs=AddStaff.objects.filter(is_active=True)
        for j in active_staffs:
            active_staff_count=active_staff_count+1
        arr.append({
            'active_student_count':active_student_count,
            'active_bus_student_count':active_bus_student_count,
            'active_hostel_student_count':active_hostel_student_count,
            'active_staff_count':active_staff_count
        })    
        return Response({'res':arr})        