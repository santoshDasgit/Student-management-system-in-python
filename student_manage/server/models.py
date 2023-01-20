
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.



class User(AbstractUser):
    USER = (
        (1,'HOD_USER'),
        (2,'STAFF_USER'),
        (3,'STUDENT_USER')
    )
    user_type = models.CharField(max_length = 90,choices=USER,default=1)
    profile_image = models.ImageField(upload_to = 'profile_pic')
    def __str__(self):
         return f'{self.username}--{self.user_type}'


class Course(models.Model):
    name = models.CharField(max_length = 99)
    create_date =  models.DateTimeField(auto_now_add = True) 
    Update =  models.DateTimeField(auto_now_add = True) 
    def __str__(self) -> str:
         return self.name


class Branch(models.Model):
    name = models.CharField(max_length = 99)
  
    create_date =  models.DateTimeField(auto_now_add = True) 
    Update =  models.DateTimeField(auto_now_add = True) 
    def __str__(self) -> str:
         return self.name

class Semester(models.Model):
    name = models.CharField(max_length = 99)
    create_date =  models.DateTimeField(auto_now_add = True) 
    Update =  models.DateTimeField(auto_now_add = True) 
    def __str__(self):
        return self.name


class Session_year(models.Model):
    session_start = models.CharField(max_length = 40)
    session_end = models.CharField(max_length = 40)
    def __str__(self) -> str:
         return f'{self.session_start} to {self.session_end}'

class Student(models.Model):

       admin = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
       address = models.CharField(max_length=200)
       gender = models.CharField(max_length = 30)
       course = models.ForeignKey(Course,on_delete = models.SET_DEFAULT,null=True,default=None)
       branch = models.ForeignKey(Branch,on_delete = models.SET_DEFAULT,null=True,default=None)
       semester = models.ForeignKey(Semester,on_delete = models.SET_DEFAULT,null=True,default=None)
       session = models.ForeignKey(Session_year,on_delete = models.SET_DEFAULT,null=True,default=None)
       ph = models.CharField(max_length = 200,default=None)
       dob = models.CharField(max_length = 300)
       father = models.CharField(max_length = 300)
       mother = models.CharField(max_length = 200)
       father_ph = models.CharField(max_length = 300)
       mother_ph = models.CharField(max_length = 300)
       create_date =  models.DateTimeField(auto_now_add = True) 
       Update =  models.DateTimeField(auto_now_add = True) 
       def __str__(self) -> str:
            return self.admin.username
       


class Teacher(models.Model):
       admin = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
       teacher_id = models.CharField(max_length = 200,default=None ,null=True, blank=True)
       address = models.CharField(max_length=200)
       gender = models.CharField(max_length = 30)
       course = models.ForeignKey(Course,on_delete = models.SET_DEFAULT,null=True,default=None)
       branch = models.ForeignKey(Branch,on_delete = models.SET_DEFAULT,null=True,default=None)
       ph = models.CharField(max_length = 200,default=None)
       dob = models.CharField(max_length = 300,default=None)
       join = models.CharField(max_length = 100,default=None)
       qualification = models.CharField(max_length=100,default=None)
       experience = models.CharField(max_length=100,default=None)
       create_date =  models.DateTimeField(auto_now_add = True) 
       Update =  models.DateTimeField(auto_now_add = True) 
       def __str__(self) -> str:
            return f'{self.admin.first_name} {self.admin.last_name}___{self.admin.username} '

class Hod(models.Model):
     branch  = models.ForeignKey(Branch,on_delete = models.CASCADE,null=True,default=None )
     hod = models.ForeignKey(Teacher,on_delete = models.SET_DEFAULT,null=True,default=None,blank=True)
     def __str__(self) -> str:
         return f'{self.branch} , {self.hod}'
       
class Subject(models.Model):
    course = models.ForeignKey(Course,on_delete = models.CASCADE,null=True,default=None)
    branch = models.ForeignKey(Branch,on_delete = models.SET_DEFAULT,null=True,default=None)
    sem = models.ForeignKey(Semester,on_delete = models.SET_DEFAULT,null=True,default=None)
    teacher = models.ForeignKey(Teacher,on_delete = models.SET_DEFAULT,null=True,blank=True,default=None)
    name = models.CharField(max_length = 100)
    class Meta:
        ordering = ('course','branch')
    def __str__(self) -> str:
         return f'{self.name} ({self.course}_{self.branch}_{self.sem}) {self.id}'





class Routine_head(models.Model):
    course = models.ForeignKey(Course,on_delete = models.CASCADE,null=True,default=None )
    branch = models.ForeignKey(Branch,on_delete = models.SET_DEFAULT,null=True,default=None )
    sem = models.ForeignKey(Semester,on_delete = models.SET_DEFAULT,null=True ,default=None)
    def __str__(self):
        return f'{self.course.name}--{self.branch.name}--{self.sem}'
    



class Routine(models.Model):
    related = models.ForeignKey(Routine_head,on_delete = models.CASCADE,default=None)
    start = models.CharField(max_length = 100 ,null=True,blank=True)
    end = models.CharField(max_length = 100 ,null=True,blank=True)
    monday = models.CharField(max_length = 100 ,null=True,blank=True)
    tuesday = models.CharField(max_length = 100 ,null=True,blank=True)
    wednesday = models.CharField(max_length = 100 ,null=True,blank=True)
    thursday = models.CharField(max_length = 100 ,null=True,blank=True)
    friday = models.CharField(max_length = 100 ,null=True,blank=True)
    saturday= models.CharField(max_length = 100 ,null=True,blank=True)
    class Meta:
        ordering = ('start',)
    def __str__(self) -> str:
         return f'{self.related.course.name}--{self.related.branch.name}--{self.related.sem}'




class Teacher_msg(models.Model):
    head = models.CharField(max_length = 100)
    messages = RichTextField(blank = True,null=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return self.head

class Teacher_see_msg(models.Model):
    msg = models.ForeignKey(Teacher_msg,on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return f'{self.msg.head}-------{self.teacher.admin.first_name}'

class Student_msg(models.Model):
    head = models.CharField(max_length = 100)
    messages = RichTextField(blank = True,null=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return self.head

class Student_see_msg(models.Model):
    msg = models.ForeignKey(Student_msg,on_delete = models.CASCADE)
    student = models.ForeignKey(Student,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return f'{self.msg.head}-------{self.student.admin.first_name}'


class teacher_leave_apply(models.Model):
    user_id = models.ForeignKey(Teacher,on_delete = models.CASCADE,null=True,blank = True)
    start = models.DateField()
    end = models.DateField()
    title = models.CharField(max_length= 50)
    msg = RichTextField(blank = True,null=True)
    status = models.BooleanField(default = None,null=True,blank = True)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return f'{self.user_id}_______{self.title}'

class Student_leave_apply(models.Model):
    user_id = models.ForeignKey(Student,on_delete = models.CASCADE,null=True,blank = True)
    start = models.DateField()
    end = models.DateField()
    title = models.CharField(max_length= 50)
    msg = RichTextField(blank = True,null=True)
    status = models.BooleanField(default = None,null=True,blank = True)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return f'{self.user_id}_______{self.title}'


class TeachersFeedback(models.Model):
    user_id = models.ForeignKey(Teacher,on_delete = models.CASCADE,null = True,blank = True)
    title = models.CharField(max_length = 200)
    msg = RichTextField()
    replay = models.CharField(max_length = 400,blank = True,null = True,default=None)
    status = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return f' TEACHER__  {self.title}'

class StudentsFeedback(models.Model):
    user_id = models.ForeignKey(Student,on_delete = models.CASCADE,null = True,blank = True)
    title = models.CharField(max_length = 200)
    msg = RichTextField()
    replay = models.CharField(max_length = 400,blank = True,null = True,default=None)
    status = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
         return f' STUDENT__  {self.title}'


class Attendance(models.Model):

    subject = models.ForeignKey(Subject,on_delete = models.CASCADE,null=True,default=None)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_DEFAULT,blank = True,null = True,default=None)
    date = models.CharField(max_length=100)
  
    def __str__(self) -> str:
         return f' {self.subject.name} {self.date}'


class Attendance_chields(models.Model):
    student = models.ForeignKey(Student,on_delete = models.CASCADE,default=None)
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE,null=True,blank = True,default=None)
    attendance = models.ForeignKey(Attendance,on_delete = models.CASCADE)
    date = models.CharField(max_length=100,blank = True,null = True,default=None)
    
    def __str__(self) -> str:    
         return f'{self.student.admin.first_name} {self.student.admin.last_name}'


class Student_online_class(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE ,blank = True,null = True,default=None)
    user = models.ForeignKey(Teacher,on_delete=models.CASCADE ,blank = True,null = True,default=None)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE ,null = True,default=None)
    link = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)
    class Meta:
        ordering = ('date',)
    def __str__(self) -> str:
         return f'{self.subject}    {self.user}'
    


class Blog(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE,blank = True,null = True)
     date = models.DateField(auto_now_add=True)
     blog_img = models.ImageField(upload_to = 'blog_img')
     head = models.CharField(max_length=400)
     description = models.CharField(max_length=200,blank=True,null=True)
     para =  RichTextField()
    
     def __str__(self) -> str:
          return f'{self.user}___{self.head}'

class Blog_comment(models.Model):
     blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
     date = models.DateField(auto_now_add=True)
     user = models.ForeignKey(User,on_delete=models.CASCADE,blank = True,null = True,default=None)
     comment = models.TextField(default=None)
     def __str__(self) -> str:
          return f'{self.blog}'
     



class Hostel(models.Model):
     block = models.CharField(max_length=100)
     room = models.CharField(max_length=200)
     no_of_bed = models.CharField(max_length=100)
     cost = models.CharField(max_length=200)
     available = models.BooleanField(default=False)
     available_bed = models.CharField(max_length=200,blank=True,null = True)
     def __str__(self) -> str:
          return f'{self.block} {self.room}'

class Hostel_student(models.Model):
    hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
         return f'{self.student} {self.hostel}'
    

    
class Transport(models.Model):
     route = models.CharField(max_length=400)
     bus_num = models.IntegerField()
     driver_name = models.CharField(max_length=400)
     driver_ph1 = models.IntegerField()
     driver_ph2 = models.IntegerField(blank=True,null=True)
     license = models.CharField(max_length=100)
     driver_address = models.CharField(max_length=300)
     def __str__(self):
         return f'{self.route}__{self.bus_num}'
     

class Group_discussion(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    user_type = models.CharField(max_length=10,default=None,blank=True,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,blank=True,null=True)
    sem = models.ForeignKey(Semester,on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to = 'group_discussion',blank=True,null=True)
    text = RichTextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
         return f'{self.user}___{self.text}'[:30]

class Group_discussion_replay(models.Model):
    gd = models.ForeignKey(Group_discussion,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to = 'group_discussion',blank=True,null=True)
    text = RichTextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
         return f'{self.gd}__{self.user}'
     



# _____________________________________Quiz______________________________________

DIF_CHOICE = (
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard')
)

class Quiz(models.Model):
    name = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE , default = '')
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE , default = '')
    sem = models.ForeignKey(Semester,on_delete=models.CASCADE , default = '')
    topic = models.CharField(max_length=120)
    num_of_qn = models.IntegerField()
    time_duration = models.IntegerField(help_text='duration of quiz in minutes')
    pass_mark = models.IntegerField(help_text="required scour to pass")
    difficulty = models.CharField(max_length=20,choices=DIF_CHOICE)
    show_qn = models.BooleanField(default=False)
    show_res = models.BooleanField(default=False)
   
    def __str__(self) -> str:
         return f'{self.name}__{self.topic}'
    def get_question(self):
        return self.quiz_qn_set.all()



class Quiz_qn(models.Model):
    text = models.CharField(max_length=300) 
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
         return f'{self.quiz.name}___{self.text}'
    def get_answer(self):
        return self.quiz_ans_set.all()


class Quiz_ans(models.Model):
    text = models.CharField(max_length=300 ,null=True,blank=True)
    correct = models.BooleanField(default=False )

    question = models.ForeignKey(Quiz_qn,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) -> str:
         return f'{self.question}____{self.text}___{self.correct}'


class Quiz_result(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    total_mark = models.IntegerField(default=0)
    score = models.FloatField()
    result_status = models.BooleanField(default=False)
    def __str__(self) -> str:
         return f'{self.user}_{self.quiz.topic}'


class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    last_date = models.CharField(max_length=200)
    online = models.BooleanField(default=False)
    offline = models.BooleanField(default=False)
    assignment_start = models.BooleanField(default=False)
    def __str__(self) -> str:
         return f'{self.subject.name}__{self.teacher.admin.first_name} {self.teacher.admin.last_name}'

class Assignment_submit_student(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name='assignment_submit_student',null=True,blank=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    file = models.FileField(upload_to='assignment',null=True,blank=True)
    offline = models.BooleanField(default=False)
    description = RichTextField(blank=True,null=True)

    def __str__(self) -> str:
         return f'{self.assignment.topic} __ {self.student.admin.first_name}'

class Assignment_result(models.Model):
    assignment = models.OneToOneField(Assignment_submit_student,related_name='assignment_results',on_delete=models.CASCADE,null=True,blank=True)
    teacher_accept = models.BooleanField(default=False)
    teacher_mark = models.IntegerField(default=0)

class StarStudent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    hod = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class Notice_teacher_to_student(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='teacher_notice')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    sem = models.ForeignKey(Semester,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)









