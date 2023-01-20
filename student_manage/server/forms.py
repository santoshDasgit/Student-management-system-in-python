
from .models import *
from django import forms



    


    


class Subject_from(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        ordering = ['branch']

class Session_year_form(forms.ModelForm):
    class Meta:
        model = Session_year
        fields = '__all__'
        widgets = {
            'session_start':forms.TextInput(attrs={'type':'number','placeholder':'yyyy'}),
            'session_end':forms.TextInput(attrs={'type':'number','placeholder':'yyyy'})
        }


class Teacher_message_form(forms.ModelForm):
    class Meta:
        model = Teacher_msg
        fields = ['head','messages']
       
        labels = {
            'head':'Title'
        }
        

class Student_message_form(forms.ModelForm):
    class Meta:
        model = Student_msg
        fields = ['head','messages']
       
        labels = {
            'head':'Title'
        }

class teacher_leave_apply_form(forms.ModelForm):
    class Meta:
        model=teacher_leave_apply
        fields = ['user_id','title','start','end','msg']
        widgets = {
            'user_id':forms.HiddenInput(),
            'start':forms.TextInput(attrs={'type':'date'}),
            'end':forms.TextInput(attrs={'type':'date'}),
        }
        labels = {
            'start':'Start date',
            'end':'End_date',
            'msg':'Message'
        }


class HodForms(forms.ModelForm):
    class Meta:
        model = Hod
        fields = ['hod']
        widgets = {
            'hod':forms.Select(attrs={'class':'form-control w-100'})

        }
        
class student_leave_apply_form(forms.ModelForm):
    class Meta:
        model=Student_leave_apply
        fields = ['user_id','title','start','end','msg']
        widgets = {
            'user_id':forms.HiddenInput(),
            'start':forms.TextInput(attrs={'type':'date'}),
            'end':forms.TextInput(attrs={'type':'date'}),
        }
        labels = {
            'start':'Start date',
            'end':'End_date',
            'msg':'Message'
        }


class Routine_headForms(forms.ModelForm):
    class Meta:
        model = Routine_head
        fields = "__all__"
        widgets = {
            'course':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'}),
            'sem':forms.Select(attrs={'class':'form-control'}),
        }
    
class Teacher_feedback_form(forms.ModelForm):
    class Meta:
        model = TeachersFeedback
        fields = ['title','msg']

class Student_feedback_form(forms.ModelForm):
    class Meta:
        model = StudentsFeedback
        fields = ['title','msg']

class Online_classForm(forms.ModelForm):
    class Meta:
        model = Student_online_class
        fields = ['semester','link','date','start_time','end_time','status']
        widgets = {
            'semester':forms.Select(attrs={'class':'form-control form-control-lg'}),
            'link':forms.TextInput(),
            'date':forms.TextInput(attrs={'type':'date'}),
            'start_time':forms.TextInput(attrs={'type':'time'}),
            'end_time':forms.TextInput(attrs={'type':'time'}),
            'status':forms.CheckboxInput(attrs={'class':'w-25'})
        }
        labels = {
            'status':'Immediately class start'
        }
    
class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['head','description','blog_img','para']
        widgets = {
             'description':forms.TextInput(attrs={'placeholder':'maximum character 200..'})
         }
        labels = {
            'para':'Description',
            'blog_img' :'Blog Image',
            'head':'Title*'
        }

class Transport_form(forms.ModelForm):
    class Meta:
        model = Transport
        fields = '__all__'
        labels = {
            'bus_num':'Bus number',
            'driver_ph1':'Driver phone1',
            'driver_ph2':'Driver phone2'
        }


class Gd_form(forms.ModelForm):
    class Meta:
        model = Group_discussion
        fields = ['image','text']

class Gd_replay_form(forms.ModelForm):
    class Meta:
        model = Group_discussion_replay
        fields = ['image','text']



class Quiz_form(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['course','branch','sem','topic','num_of_qn','time_duration','pass_mark','difficulty','show_qn','show_res']
        widgets = {
            'name':forms.Select(attrs={'class':'d-none'}),
            'difficulty':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'}),
            'sem':forms.Select(attrs={'class':'form-control'}),
            'course':forms.Select(attrs={'class':'form-control'}),
              
        }
        labels = {
            'name':'',
            'pass_mark':'Pass mark in percentage',
            'show_qn':'Start Exam now',
            'show_course':'Currently show results',
            'time_duration':'Time duration in Minutes'
        }
        
     
class Quiz_qn_form(forms.ModelForm):
    class Meta:
        model = Quiz_qn
        fields = ['text']
        labels = {
            'text':'Questions add'
        }


class Teacher_profile_form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('address','gender','course','branch','ph','dob','qualification','experience')
        widgets = {
            'course':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'})
        }

class Student_profile_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('address','gender','course','branch','semester','session','ph','dob','father','mother','father_ph','mother_ph')
        widgets = {
            'course':forms.Select(attrs={'class':'form-control','readonly': 'readonly'}),
            'branch':forms.Select(attrs={'class':'form-control','readonly': 'readonly'}),
            'semester':forms.Select(attrs={'class':'form-control','readonly': 'readonly'}),
            'session':forms.Select(attrs={'class':'form-control','readonly': 'readonly'}),
            'dob':forms.DateTimeInput(),
            'ph':forms.NumberInput(),
            'father_ph':forms.NumberInput(),
            'mother_ph':forms.NumberInput(),
        }


class Assignment_create_form(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        widgets = {
            'teacher':forms.HiddenInput(),
            'subject':forms.Select(attrs={'class':'form-control'}),
            'sem':forms.Select(attrs={'class':'form-control'}),
            'last_date':forms.TextInput(attrs={'type':'date'})
        }

class Assignment_upload_student_form(forms.ModelForm):
    class Meta:
        model = Assignment_submit_student
        fields = ['file','offline','description']

class Assignment_resultForm(forms.ModelForm):
    class Meta:
        model = Assignment_result
        fields = ['teacher_accept','teacher_mark']

class Notice_teacher_to_student_Form(forms.ModelForm):
    class Meta:
        model =Notice_teacher_to_student
        fields = ['title','file','course','branch','sem']
        widgets = {
            'course':forms.Select(attrs={'class':'form-control'}),
             'branch':forms.Select(attrs={'class':'form-control'}),
             'sem':forms.Select(attrs={'class':'form-control'}),
        }


       
     
