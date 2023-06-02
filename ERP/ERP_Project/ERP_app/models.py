# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class SchoolInfo(models.Model):
    created=models.DateField(auto_now_add = True)
    school_name=models.CharField(max_length=100,null=True)
    school_address1=models.CharField(max_length=500,null=True)
    school_address2=models.CharField(max_length=500,null=True)
    school_mobile1=models.CharField(max_length=12,null=True)
    school_mobile2=models.CharField(max_length=12,null=True)
    school_email=models.EmailField(max_length=50,null=True)
    school_web=models.CharField(max_length=100,null=True)
    school_img = models . ImageField (upload_to = 'static/images', null = True)
    school_logo = models . ImageField (upload_to = 'static/images', null = True)

class AddClass(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    year=models.CharField(max_length=20, null=True)
    class_name = models.CharField(max_length=20 , null = True)
    class_fee = models.CharField(max_length=20 , null = True,default=0)
    class_fee_inst = models.CharField(max_length=20 , null = True)

class BusRoot(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    year=models.CharField(max_length=20, null=True)
    bus_name = models.CharField(max_length=50 , null = True)
    root_name = models.CharField(max_length=50 , null = True)
    root_fee = models.CharField(max_length=20 , null = True,default=0)
    root_inst = models.CharField(max_length=20 , null = True)

class AddSection(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    section_name = models.CharField(max_length=20 , null = True)

class AddHostel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    year=models.CharField(max_length=20, null=True)
    hostel_name = models.CharField(max_length=20 , null = True)
    hostel_fee = models.CharField(max_length=20 , null = True,default=0)
    hostel_fee_inst = models.CharField(max_length=20 , null = True)
    hostel_instruction = models.CharField(max_length=1000 , null = True)

class Student_type(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    student_type_name = models.CharField(max_length=20 , null = True)

class Reception(models.Model):
    created = models . DateField(auto_now_add = True,null = True)
    date_of_enq = models . DateField (null = True)
    student_name = models.CharField (max_length = 100 , null = True)
    class_name = models.ForeignKey(AddClass, related_name='reception',null=True,blank=False,on_delete=models.CASCADE)
    gender = models . CharField(max_length=10 , null = True)
    date_of_birth = models . DateField (null = True)
    father_name = models . CharField (max_length = 100 , null = True)
    mother_name = models . CharField (max_length = 100 , null = True)
    father_mobile_no = models . CharField (max_length=100 , null = True)
    mother_mobile_no = models . CharField (max_length=100 , null = True)
    temp_address = models . TextField (max_length = 5000 , null=True)
    permanent_address = models . TextField (max_length = 5000 , null=True)
    testDate = models.DateField(auto_now_add = False,null = True)
    testTime = models.DateTimeField(auto_now_add = False,null = True)
    # studentImage = models . ImageField (upload_to = 'static/images', null = True)
    # studentAadhar = models . ImageField (upload_to = 'static/images', null = True)
    # studentDOBCer = models . ImageField (upload_to = 'static/images', null = True)
    # studentTC = models . ImageField (upload_to = 'static/images', null = True)

class Admissions_form(models.Model):
    reception = models.ForeignKey(Reception, related_name='admissions',null=True,blank=False,on_delete=models.CASCADE)
    bus_root = models.ForeignKey(BusRoot, related_name='admissions',null=True,blank=False,on_delete=models.CASCADE)
    section = models.ForeignKey(AddSection, related_name='admissions',null=True,blank=False,on_delete=models.CASCADE)
    hostel = models.ForeignKey(AddHostel, related_name='admissions',null=True,blank=False,on_delete=models.CASCADE)
    student_type = models.ForeignKey(Student_type, related_name='admissions',null=True,blank=False,on_delete=models.CASCADE)
    # extra = models.ForeignKey(ExtraFeeStructure, related_name='admissions',null=True,blank=False,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add = True)
    admission_date = models.DateField(auto_now_add = False)
    admission_no = models . CharField (max_length = 20 , null=True)
    roll_no = models.CharField(max_length=200 , null = True)
    # hostelTyoe = models.BooleanField(default=False)
    caste = models.CharField(max_length=200 , null = True)
    religion = models.CharField(max_length=200 , null = True)
    father_occupation = models . CharField (max_length = 100 , null = True)
    father_qualification = models . CharField (max_length = 100 , null = True)
    alternate_mobile_no = models . CharField (max_length=100 , null = True)
    mother_occupation = models . CharField (max_length = 100 , null = True)
    mother_qualification = models . CharField (max_length = 100 , null = True)
    alternate_mobile_no = models . CharField (max_length=100 , null = True)
    studentImage = models . ImageField (upload_to = 'static/images', null = True)
    studentAadhar = models . ImageField (upload_to = 'static/images', null = True)
    studentDOBCerficate = models . ImageField (upload_to = 'static/images', null = True)
    studentTC = models . ImageField (upload_to = 'static/images', null = True)
    is_active=models.BooleanField(default=True)

    

class AddDepartment(models.Model):
    created=models.DateField(auto_now_add = True)
    department_name=models.CharField(max_length=50,null=True)

class AddStaff(models.Model):
    department = models.ForeignKey(AddDepartment, related_name='addstaff',null=True,blank=False,on_delete=models.CASCADE)
    staff_name = models.CharField (max_length = 100 , null = True)
    date_of_birth = models . DateField (null = True)
    email = models . EmailField (max_length = 100 , null = True)
    mobile_no = models . CharField (max_length=100 , null = True)
    gender = models . CharField(max_length=10 , null = True)
    joining_date = models.DateField(auto_now_add = True , null = True)
    designation = models.CharField (max_length = 100 , null = True)
    basic_salary = models.CharField (max_length = 100 , null = True)
    subject = models . CharField(max_length=50 , null = True)
    father_name = models . CharField (max_length = 100 , null = True)
    mother_name = models . CharField (max_length = 100 , null = True)
    husband_name = models . CharField (max_length = 100 , null = True)
    staff_qualification = models . CharField (max_length = 100 , null = True)
    # bankSal = models.CharField (max_length = 100 , null = True)
    temp_address = models . TextField (max_length = 5000 , null=True)
    permanent_address = models . TextField (max_length = 5000 , null=True)
    alternate_mobile_no = models . CharField (max_length=100 , null = True)
    staffImage = models . ImageField (upload_to = 'static/images', null = True)
    created = models.DateField(auto_now_add = True , null = True)
    is_active=models.BooleanField(default=True)


class ExtraFeeStructure(models.Model):
    class_name = models.ForeignKey(AddClass, related_name='extraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)
    student_type = models.ForeignKey(Student_type, related_name='extraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    fee_name = models.CharField(max_length=50 , null = True)
    fee_amount = models.CharField(max_length=200 , null = True,default=0)
    month=models.CharField(max_length=20, null=True)
    year=models.CharField(max_length=20, null=True)
    created=models.DateField(auto_now_add = True)

class ExtraFeeDiscount(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='extraFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    extra_fee_structure = models.ForeignKey(ExtraFeeStructure, related_name='extraFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    discount_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    year=models.CharField(max_length=20, null=True)
    main_amount=models.CharField(max_length=500,null=True)
    discounted_amount=models.CharField(max_length=500,null=True)
    final_amount=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)
    created=models.DateField(auto_now_add = True)

class ClassFeeDiscount(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='classFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    discount_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    year=models.CharField(max_length=20, null=True)
    main_amount=models.CharField(max_length=500,null=True)
    discounted_amount=models.CharField(max_length=500,null=True)
    final_amount=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)
    created=models.DateField(auto_now_add = True)

class HostelFeeDiscount(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='hostelFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    discount_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    year=models.CharField(max_length=20, null=True)
    main_amount=models.CharField(max_length=500,null=True)
    discounted_amount=models.CharField(max_length=500,null=True)
    final_amount=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)
    created=models.DateField(auto_now_add = True)

class BusFeeDiscount(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='busFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    discount_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    year=models.CharField(max_length=20, null=True)
    main_amount=models.CharField(max_length=500,null=True)
    discounted_amount=models.CharField(max_length=500,null=True)
    final_amount=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)
    created=models.DateField(auto_now_add = True)

class HostelExtraFeeStructure(models.Model):
    student_type = models.ForeignKey(Student_type, related_name='hostelExtraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    fee_name = models.CharField(max_length=50 , null = True)
    fee_amount = models.CharField(max_length=200 , null = True,default=0)
    month=models.CharField(max_length=20, null=True)
    year=models.CharField(max_length=20, null=True)
    created=models.DateField(auto_now_add = True)

class HostelExtraFeeDiscount(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='hostelextraFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    hostel_extra_fee_structure = models.ForeignKey(HostelExtraFeeStructure, related_name='hostelextraFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    discount_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    year=models.CharField(max_length=20, null=True)
    main_amount=models.CharField(max_length=500,null=True)
    discounted_amount=models.CharField(max_length=500,null=True)
    final_amount=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)
    created=models.DateField(auto_now_add = True)

class Receipt(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
    class_fee_discount = models.ForeignKey(ClassFeeDiscount, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
    bus_fee_discount= models.ForeignKey(BusFeeDiscount, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
    
    created=models.DateField(auto_now_add = True)
    receipt_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    year=models.CharField(max_length=20, null=True)
    issued_by=models.CharField(max_length=50,null=True)

    class_fee=models.CharField(max_length=500,null=True)
    discounted_class_fee=models.CharField(max_length=500,null=True)
    class_payable_fee=models.CharField(max_length=500,null=True)
    class_paid_fee=models.CharField(max_length=500,null=True)
    class_dues=models.CharField(max_length=500,null=True)

    bus_fee=models.CharField(max_length=500,null=True)
    discounted_bus_fee=models.CharField(max_length=500,null=True)
    bus_payable_fee=models.CharField(max_length=500,null=True)
    bus_paid_fee=models.CharField(max_length=500,null=True)
    bus_dues=models.CharField(max_length=500,null=True)

    total_amount=models.CharField(max_length=500,null=True)
    total_discounted_amount=models.CharField(max_length=500,null=True)
    total_payble_amount=models.CharField(max_length=500,null=True)
    previous_bill_current_month_paid_amount=models.CharField(default=0,max_length=500,null=True)
    paid_amount=models.CharField(max_length=500,null=True)
    total_dues=models.CharField(max_length=500,null=True)

class Receipt_for_ExtraFee(models.Model):
    receipt = models.ForeignKey(Receipt, related_name='receipt_for_extraFee',null=True,blank=False,on_delete=models.CASCADE)
    extra_fee_structure = models.ForeignKey(ExtraFeeStructure, related_name='receipt_for_extraFee',null=True,blank=False,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add = True)
    extra_fee_name=models.CharField(max_length=500,null=True)
    extra_fee=models.CharField(default=0,max_length=500,null=True)
    discounted_extra_fee=models.CharField(default=0,max_length=500,null=True)
    payable_extra_fee=models.CharField(default=0,max_length=500,null=True)
    paid_extra_fee=models.CharField(default=0,max_length=500,null=True)
    extra_fee_dues=models.CharField(default=0,max_length=500,null=True)

class Hostel_Receipt(models.Model):
    admission = models.ForeignKey(Admissions_form, related_name='hostel_receipt',null=True,blank=False,on_delete=models.CASCADE)
    hostel_fee_discount = models.ForeignKey(HostelFeeDiscount, related_name='hostel_receipt',null=True,blank=False,on_delete=models.CASCADE)
    
    created=models.DateField(auto_now_add = True)
    receipt_name=models.CharField(max_length=50,null=True)
    month=models.CharField(max_length=50,null=True)
    issued_by=models.CharField(max_length=50,null=True)

    hostel_fee=models.CharField(max_length=500,null=True)
    discounted_hostel_fee=models.CharField(max_length=500,null=True)
    hostel_payable_fee=models.CharField(max_length=500,null=True)
    hostel_paid_fee=models.CharField(max_length=500,null=True)
    hostel_dues=models.CharField(max_length=500,null=True)

    total_amount=models.CharField(max_length=500,null=True)
    total_discounted_amount=models.CharField(max_length=500,null=True)
    total_payble_amount=models.CharField(max_length=500,null=True)
    previous_bill_current_month_paid_amount=models.CharField(default=0,max_length=500,null=True)
    paid_amount=models.CharField(max_length=500,null=True)
    total_dues=models.CharField(max_length=500,null=True)


    

    
    
######################################################

# class ExtraFeePaid(models.Model):
    # admissions = models.ForeignKey(Admissions,null=True,blank=False,on_delete=models.CASCADE)
    # extrafeestructure = models.ForeignKey(ExtraFeeStructure,null=True,blank=False,on_delete=models.CASCADE)
    # paid_amt = models . CharField (max_length=100 , null = True)
    # dues_amt = models . CharField (max_length=100 , null = True)

# class IncomeMode(models.Model):
    # created = models.DateField(auto_now_add = True)
    # mode_name = models.CharField(max_length=20 , null = True)
    # mode_type = models.CharField(max_length=20 , null = True)

# class ExepenseMode(models.Model):
    # created = models.DateField(auto_now_add = True)
    # mode_name = models.CharField(max_length=20 , null = True)
    # mode_type = models.CharField(max_length=20 , null = True)

# class Income(models.Model):
    # incomemode = models.ForeignKey(IncomeMode, related_name='income',null=True,blank=False,on_delete=models.CASCADE)
    # created = models.DateField(auto_now_add = True)
    # income_details = models.TextField(max_length=2000 , null = True)
    # date = models.DateField(auto_now_add = True)
    # amount = models.CharField(max_length=200 , null = True)
    # goods = models.CharField(max_length=2000 , null = True)
    # cheque_no = models.CharField(max_length=200 , null = True)
    # bank_name= models.CharField(max_length=200 , null = True)
    # descrption=models.TextField(max_length=2000 , null = True)
    # income_type = models.CharField(max_length=20 , null = True)

# class Expense(models.Model):
    # expenseMode = models.ForeignKey(ExepenseMode, related_name='expense',null=True,blank=False,on_delete=models.CASCADE)
    # created = models.DateField(auto_now_add = True)
    # expense_details = models.TextField(max_length=2000 , null = True)
    # date = models.DateField(auto_now_add = True)
    # amount = models.CharField(max_length=200 , null = True)
    # expense_type = models.CharField(max_length=20 , null = True)
    # cheque_no = models.CharField(max_length=200 , null = True)
    # bank_name= models.CharField(max_length=200 , null = True)

# class AddBank(models.Model):
    # created = models.DateField(auto_now_add = True)
    # bank_name = models.CharField(max_length=50 , null = True)
    # acc_no = models.CharField(max_length=30 , null = True)
    # ifsc = models.CharField(max_length=30 , null = True)
    # address = models.TextField(max_length=2000 , null = True)

# class BankDeposite(models.Model):
    # addbank = models.ForeignKey(AddBank, related_name='bankdeposite',null=True,blank=False,on_delete=models.CASCADE)
    # created = models.DateField(auto_now_add = True)
    # depo_details = models.TextField(max_length=2000 , null = True)
    # date = models.DateField(auto_now_add = True)
    # amount = models.CharField(max_length=200 , null = True)
    # income_type = models.CharField(max_length=20 , null = True)
    # cheque_no = models.CharField(max_length=200 , null = True)
    # bank_name= models.CharField(max_length=200 , null = True )
    # depo_name= models.CharField(max_length=200 , null = True)

# class BankWithdraw(models.Model):
    # addbank = models.ForeignKey(AddBank, related_name='bankwithdraw',null=True,blank=False,on_delete=models.CASCADE)
    # created = models.DateField(auto_now_add = True)
    # with_details = models.TextField(max_length=2000 , null = True)
    # date = models.DateField(auto_now_add = True)
    # amount = models.CharField(max_length=200 , null = True)
    # income_type = models.CharField(max_length=20 , null = True)
    # cheque_no = models.CharField(max_length=200 , null = True)
    # bank_name= models.CharField(max_length=200 , null = True )
    # depo_name= models.CharField(max_length=200 , null = True)

# class AddExamTerm(models.Model):
    # created=models.DateField(auto_now_add = True)
    # term_name=models.CharField(max_length=50,null=True)

# class AddExamSubject(models.Model):
    # addclass = models.ForeignKey(AddClass, related_name='addexamsubject',null=True,blank=False,on_delete=models.CASCADE)
    # examterm = models.ForeignKey(AddExamTerm, related_name='addexamsubject',null=True,blank=False,on_delete=models.CASCADE)
    # created=models.DateField(auto_now_add = True)
    # subject1=models.CharField(max_length=50,null=True)
    # marks1=models.CharField(max_length=50,null=True)
    # subject2=models.CharField(max_length=50,null=True)
    # marks2=models.CharField(max_length=50,null=True)
    # subject3=models.CharField(max_length=50,null=True)
    # marks3=models.CharField(max_length=50,null=True)
    # subject4=models.CharField(max_length=50,null=True)
    # marks4=models.CharField(max_length=50,null=True)
    # subject5=models.CharField(max_length=50,null=True)
    # marks5=models.CharField(max_length=50,null=True)
    # subject6=models.CharField(max_length=50,null=True)
    # marks6=models.CharField(max_length=50,null=True)
    # subject7=models.CharField(max_length=50,null=True)
    # marks7=models.CharField(max_length=50,null=True)
    # subject8=models.CharField(max_length=50,null=True)
    # marks8=models.CharField(max_length=50,null=True)
    # subject9=models.CharField(max_length=50,null=True)
    # marks9=models.CharField(max_length=50,null=True)
    # subject10=models.CharField(max_length=50,null=True)
    # marks10=models.CharField(max_length=50,null=True)
    # subject11=models.CharField(max_length=50,null=True)
    # marks11=models.CharField(max_length=50,null=True)
    # subject12=models.CharField(max_length=50,null=True)
    # marks12=models.CharField(max_length=50,null=True)
    # subject13=models.CharField(max_length=50,null=True)
    # marks13=models.CharField(max_length=50,null=True)
    # subject14=models.CharField(max_length=50,null=True)
    # marks14=models.CharField(max_length=50,null=True)
    # subject15=models.CharField(max_length=50,null=True)
    # marks15=models.CharField(max_length=50,null=True)

# class ClassFeeDiscount(models.Model):
    # addclass = models.ForeignKey(AddClass, related_name='classFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    # addsection = models.ForeignKey(AddSection, related_name='classFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    # addadmission = models.ForeignKey(Admissions, related_name='classFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)

    # created=models.DateField(auto_now_add = True)
    # disc_name=models.CharField(max_length=50,null=True)
    # m_amount=models.CharField(max_length=500,default=0)
    # amount=models.CharField(max_length=500,default=0)
    # month=models.CharField(max_length=50,null=True)
    # t_amount=models.CharField(max_length=50,null=True,default=0)

# class BusFeeDiscount(models.Model):
    # addclass = models.ForeignKey(AddClass, related_name='busFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    # addsection = models.ForeignKey(AddSection, related_name='busFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    # addadmission = models.ForeignKey(Admissions, related_name='busFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)

    # created=models.DateField(auto_now_add = True)
    # disc_name=models.CharField(max_length=50,null=True)
    # m_amount=models.CharField(max_length=500,default=0)
    # amount=models.CharField(max_length=500,null=True)
    # month=models.CharField(max_length=50,null=True)
    # t_amount=models.CharField(max_length=50,null=True,default=0)

# class ExtraFeeDiscount(models.Model):
#     addadmission = models.ForeignKey(Admissions, related_name='extraFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
#     created=models.DateField(auto_now_add = True)
#     disc_name=models.CharField(max_length=50,null=True)
#     amount=models.CharField(max_length=500,null=True)
#     month=models.CharField(max_length=50,null=True)
#     t_amount=models.CharField(max_length=50,null=True)

# class HostelFeeDiscount(models.Model):
    # addadmission = models.ForeignKey(Admissions, related_name='hostelFeeDiscount',null=True,blank=False,on_delete=models.CASCADE)
    # created=models.DateField(auto_now_add = True)
    # disc_name=models.CharField(max_length=50,null=True)

    # amount=models.CharField(max_length=500,null=True)
    # month=models.CharField(max_length=50,null=True)
    # t_amount=models.CharField(max_length=50,null=True)

# class ExtraFeeStructure(models.Model):
#     # reception = models.ForeignKey(Reception, related_name='extraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)
#     addclass = models.ForeignKey(AddClass, related_name='extraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)
#     # addadmission = models.ForeignKey(Admissions, related_name='extraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add = True)
#     fee_name = models.CharField(max_length=50 , null = True)
#     extra_fee = models.CharField(max_length=200 , null = True)
#     month=models.CharField(max_length=20, null=True)
#     stdType = models.TextField(default = 'NEW' , choices = STUDENTTYPE_CHOICES)

# class Receipt(models.Model):
#     addclass = models.ForeignKey(AddClass, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
#     addsection = models.ForeignKey(AddSection, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
#     addadmission = models.ForeignKey(Admissions, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
#     classfeediscount = models.ForeignKey(ClassFeeDiscount, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)
#     busfeediscount = models.ForeignKey(BusFeeDiscount, related_name='receipt',null=True,blank=False,on_delete=models.CASCADE)

#     created=models.DateField(auto_now_add = True)
#     receipt_name=models.CharField(max_length=50,null=True)
#     month=models.CharField(max_length=50,null=True)
#     issuedBy=models.CharField(max_length=50,null=True)
#     main_amount=models.CharField(max_length=500,null=True)
#     paid_amount=models.CharField(max_length=500,null=True)
#     t_amount=models.CharField(max_length=500,null=True)
#     dues=models.CharField(max_length=500,null=True)
#     disc_amt=models.CharField(max_length=500,null=True)
#     Payble_amt=models.CharField(max_length=500,null=True)

#     cls_fee=models.CharField(max_length=500,null=True)
#     cls_pay_fee=models.CharField(max_length=500,null=True)
#     cls_dues=models.CharField(max_length=500,null=True)

#     bs_fee=models.CharField(max_length=500,null=True)
#     bs_pay_fee=models.CharField(max_length=500,null=True)
#     bs_dues=models.CharField(max_length=500,null=True)

#     ext_fee=models.CharField(max_length=500,null=True)
#     ext_pay_fee=models.CharField(max_length=500,null=True)
#     ext_dues=models.CharField(max_length=500,null=True)
#     today_pay=models.CharField(max_length=500,null=True)

# class HostelReceipt(models.Model):
    # addadmission = models.ForeignKey(Admissions, related_name='hostelReceipt',null=True,blank=False,on_delete=models.CASCADE)
    # created=models.DateField(auto_now_add = True)
    # receipt_name=models.CharField(max_length=50,null=True)
    # month=models.CharField(max_length=50,null=True)
    # issuedBy=models.CharField(max_length=50,null=True)
    # main_amount=models.CharField(max_length=500,null=True)
    # paid_amount=models.CharField(max_length=500,null=True)
    # t_amount=models.CharField(max_length=500,null=True)
    # dues=models.CharField(max_length=50,null=True)
    # disc_amt=models.CharField(max_length=50,null=True)
    # Payble_amt=models.CharField(max_length=50,null=True)

# class Final_amt(models.Model):
    # addadmission = models.ForeignKey(Admissions, related_name='extraFeeStructure',null=True,blank=False,on_delete=models.CASCADE)

    # created = models.DateTimeField(auto_now_add = True)
    # amt = models.CharField(max_length=200 , null = True,default=0)
    # month=models.CharField(max_length=20, null=True)
