
from datetime import datetime,date
from django import template
from server.models import *

register = template.Library()

@register.simple_tag
def age(dob):
    if dob == '' or dob == None:
        return dob
    else:
        date_string = dob
        dob = datetime.strptime(date_string,'%Y-%m-%d')

        def calculateAge(birthDate):
            today = date.today()
            age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    
            return age
        return(calculateAge(date(dob.year,2,3)))

@register.simple_tag
def subject_name(data):
    try:
        if data.isnumeric():
            return Subject.objects.get(pk = int(data)).name
        else:
            return data
    except:
        return None

@register.simple_tag
def string(data):
    return str(data)

@register.simple_tag
def teacher_name(data):
    if data.isnumeric():
        try:
            if Subject.objects.get(pk = int(data)).teacher is not None:
                return f'{Subject.objects.get(pk = int(data)).teacher.admin.first_name} {Subject.objects.get(pk = int(data)).teacher.admin.last_name}'
            else:
                return None
        except:
            return None
    else:
        return ''

@register.simple_tag
def teacher_ide(data):
        if data.isnumeric():
            try:
                if Subject.objects.get(pk = int(data)).teacher is not None:
                    return int(Subject.objects.get(pk = int(data)).teacher.admin.pk)
                else:
                    return 'Not mention'
            except:
                return None
        else:
            return 0

@register.simple_tag
def msg_deactivate(msg_id,user):
        try:
             Teacher_see_msg.objects.get(msg=Teacher_msg.objects.get(id = msg_id) ,teacher = Teacher.objects.get(admin = User.objects.get(id=user)))
             return True
        except:
            return False


@register.simple_tag
def stu_msg_deactivate(msg_id,user):
        try:
             Student_see_msg.objects.get(msg=Student_msg.objects.get(id = msg_id) ,student = Student.objects.get(admin = User.objects.get(id=user)))
             return True
        except:
            return False

@register.simple_tag
def leave_duration(start,end):
        return f'{end-start}'.strip(', 0:00:00')
           

@register.simple_tag
def attendance_student(id):
        data = Attendance_chields.objects.filter(attendance = Attendance.objects.get(id = id))
        return data

@register.simple_tag
def attendance_show(id):
    try:
        data = Attendance.objects.filter(subject = Subject.objects.get(id = id))
        return data
    except:
        return 'Empty class Take'

@register.simple_tag
def attendance_children(stu,sub):
    try:
        
        data = Attendance_chields.objects.filter(student = Student.objects.get(admin = stu), subject = Subject.objects.get(id = sub))
        
        return data
    except:
        return 'Empty class Take'

@register.simple_tag
def gd_student(user):
    return f'({Student.objects.get(admin = user).course},{Student.objects.get(admin = user).branch},{Student.objects.get(admin = user).semester}_sem)'


@register.simple_tag
def gd_student_replays(data):
    return Group_discussion_replay.objects.filter(gd = data)

@register.simple_tag
def float_into_dec(data):
    return round(data,2)
   
@register.simple_tag
def quiz_pass_fell(mark,pass_mark):
    if mark<pass_mark:
        return False
    else:
        return True


@register.simple_tag
def student_assignment_check(user,template):
    if Assignment_submit_student.objects.filter(assignment = Assignment.objects.get(id = template),student = Student.objects.get(admin = user)).exists():
        return True
    else:
        return False


@register.simple_tag
def student_assignment_result_check(id):
    if Assignment_result.objects.filter(assignment = Assignment_submit_student.objects.get(id = id)).exists():
        return True
    else:
        return False


@register.simple_tag
def hod_or_not_check(user):
    if Hod.objects.filter(hod = Teacher.objects.get(admin = user)).exists():
        return True
    else:
        return False




 