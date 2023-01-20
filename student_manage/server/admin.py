
from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(User,UserAdmin)

admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Session_year)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Hod)
admin.site.register(Subject)
admin.site.register(Routine)
admin.site.register(Routine_head)
admin.site.register(Teacher_msg)
admin.site.register(Teacher_see_msg)
admin.site.register(Student_msg)
admin.site.register(Student_see_msg)
admin.site.register(teacher_leave_apply)
admin.site.register(Student_leave_apply)
admin.site.register(TeachersFeedback)
admin.site.register(StudentsFeedback)
admin.site.register(Attendance)
admin.site.register(Attendance_chields)
admin.site.register(Student_online_class)
admin.site.register(Blog)
admin.site.register(Blog_comment)
admin.site.register(Hostel)
admin.site.register(Hostel_student )
admin.site.register(Transport )
admin.site.register(Group_discussion)
admin.site.register(Group_discussion_replay)

admin.site.register(Quiz)
admin.site.register(Quiz_ans)
admin.site.register(Quiz_qn)
admin.site.register(Quiz_result)

admin.site.register(Assignment)
admin.site.register(Assignment_result)
admin.site.register(Assignment_submit_student)

admin.site.register(StarStudent)
admin.site.register(Notice_teacher_to_student)



  


