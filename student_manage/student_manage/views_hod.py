
from turtle import update
from urllib import request
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from server.models import *
from django.db.models import Q
from django.views import View
from server.forms import *



@login_required(login_url='/')
def dashboard(request):
    data = {
            'student':Student.objects.all(),
            'teacher':Teacher.objects.all(),
            'course':Course.objects.all(),
            'branch':Branch.objects.all(),
            'subject':Subject.objects.all(),
            'sem':Semester.objects.all(),
            'teacher_leave_condition':len(teacher_leave_apply.objects.filter(status = None)) <=0,
            'teacher_leave_counter':len(teacher_leave_apply.objects.filter(status = None)),
            'student_leave_condition':len(Student_leave_apply.objects.filter(status = None)) <=0,
            'student_leave_counter':len(Student_leave_apply.objects.filter(status = None)),
            'teacher_feedback_counter':len(TeachersFeedback.objects.filter(status = False)),
            'student_feedback_counter':len(StudentsFeedback.objects.filter(status = False)),
            'star_student':StarStudent.objects.all()

    }
    return render(request,'hod/dashboard.html',data)

@login_required(login_url='/')
def student_add(request):
    if request.method  == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        reg = request.POST.get('id')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        course = request.POST.get('course')
        sem = request.POST.get('sem')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        dob = request.POST.get('dob')
        mob = request.POST.get('mob')
        img = request.FILES.get('img',None)
        father = request.POST.get('father')
        father_ph = request.POST.get('father_ph')
        mother = request.POST.get('mother')
        mother_ph = request.POST.get('mother_ph')
        address = request.POST.get('address')
        if User.objects.filter(username = reg).exists():
 
            messages.error(request,f"This is User ' {User.objects.get(username = reg).first_name} ' already exit   ")
        else:
            user = User(
                first_name = fname,
                last_name = lname,
                user_type = 3,
                username = reg,
                profile_image = img,
                email = email
            )

            
            user.set_password(password)
            user.save()
            

            student = Student(
                admin = user,
                address = address,
                gender = gender,
                course = Course.objects.get(id = course),
                branch = Branch.objects.get(id = branch),
                semester = Semester.objects.get(id = sem),
                session = Session_year.objects.get(id = year),
                dob = dob,
                ph = mob,
                father = father,
                mother = mother,
                father_ph = father_ph,
                mother_ph = mother_ph,
            )

            student.save()
            messages.success(request,'User created Successfully')

    else:
        pass

    data = {   
        'branch':Branch.objects.all(),
        'sem':Semester.objects.all(),
        'year':Session_year.objects.all(),
        'course':Course.objects.all()
    }
    return render(request,'hod/student_add.html',data)


@login_required(login_url='/')
def student_list(request):
  
     obj = Student.objects.all().order_by('-course','branch')
 
     if request.method == 'POST':
         search = request.POST.get('search')
         branch = request.POST.get('branch')
         course = request.POST.get('course')
         sem = request.POST.get('sem')
         year = request.POST.get('year')


         if search != "" :
            string = search.split()
            user = User.objects.filter(Q(username__icontains = string[0]) |  Q(last_name__icontains = string[0]) | Q(first_name__icontains = string[0]) | Q(email__icontains=string[0] ) )
            obj = Student.objects.filter(admin__in = user)

         if branch != "":
   
            try:
                obj = Student.objects.filter(branch__in = Branch.objects.filter(pk = branch))
            except:
                pass
            
            
         if course != "":
 
            try:
                obj = Student.objects.filter(course__in = Course.objects.filter(pk = course))
            except:
                pass
        
         if sem != "":
            
            try:
                obj = Student.objects.filter(semester__in = Semester.objects.filter(pk = sem))
            except:
                pass
        
         if year != "":
         
            obj = Student.objects.filter(session__in = Session_year.objects.filter(pk = year))
        
            
            
        
     data = {   
        'branch':Branch.objects.all(),
        'sem':Semester.objects.all(),
        'year':Session_year.objects.all(),
        'course':Course.objects.all(),
        'data': obj
    }
     return render(request,'hod/student_list.html',data)


@login_required(login_url='/')
def student_details(request,url):
    data = {
        'data':Student.objects.get(pk = url),
       
    }
    
    return render(request,'hod/student_details.html',data)


@login_required(login_url='/')
def student_update(request,url):
    data = {
        'data':Student.objects.get(pk=url),
        'student':Student.objects.all(),
        'course':Course.objects.all(),
         'year':Session_year.objects.all(),
          'sem':Semester.objects.all(),
         'branch':Branch.objects.all(),
         'info1':User.objects.get(id = Student.objects.get(pk = url).admin.id)
    }
    if request.method  == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        reg = request.POST.get('id')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        course = request.POST.get('course')
        sem = request.POST.get('sem')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        dob = request.POST.get('dob')
        mob = request.POST.get('mob')
        img = request.FILES.get('img',None)
        father = request.POST.get('father')
        father_ph = request.POST.get('father_ph')
        mother = request.POST.get('mother')
        mother_ph = request.POST.get('mother_ph')
        address = request.POST.get('address')
       
        user = User.objects.get(id = Student.objects.get(pk = url).admin.id)
        user.first_name = fname
        user.last_name = lname
        user.user_type = 3
        user.username = reg
        if not img is None or img is "":
            user.profile_image = img
        user.email = email
        
        if password == None or password == "":
            user.save()
        else:
            user.set_password(password)
            user.save()
        student = Student(
                admin = user,
                address = address,
                gender = gender,
                course = Course.objects.get(id = course),
                branch = Branch.objects.get(id = branch),
                semester = Semester.objects.get(id = sem),
                session = Session_year.objects.get(id = year),
                dob = dob,
                ph = mob,
                father = father,
                mother = mother,
                father_ph = father_ph,
                mother_ph = mother_ph,
                create_date = Student.objects.get(pk = url).create_date,
                Update =  Student.objects.get(pk = url).Update
        )

        student.save()
        messages.success(request,f'  Update "{reg}" User Successfully refresh the page')

    return render(request,'hod/student_update.html',data)


@login_required(login_url='/')
def remove_students(request,url):
    user = User.objects.filter(id=url)
    Student.objects.get(admin__in = user).delete()
    user.delete()
    return redirect('student_list')
    

@login_required(login_url='/')
def course_add(request):  
    data = {
        'data':Course.objects.all()
    }
    if request.method == 'POST':
        fm = request.POST['name']
        if fm == "" or fm == None:
            messages.error(request,'blank input')
        else:
            if Course.objects.filter(name=fm).exists():
                messages.warning(request,'course already mention ')
            else:
                Course(name = fm).save()
            
    return render(request,'hod/course_add.html',data)    

@login_required(login_url='/')
def course_remove(request,url):
    try:
        Course.objects.get(id = url).delete()
        return redirect('course_add')
    except:
        messages.error('Not possible to removing the items berceuse Foreign Key is there')
        return redirect('course_add')

@login_required(login_url='/')
def course_edit(request,url):
    if request.method =='POST':
        fm = request.POST['name']
        if fm == "" or fm == None:
            messages.error(request,'Blank form Try again')
        else:
            course =  Course.objects.get(id = url)
            course.name = fm
            course.save()
            return redirect('course_add')

    return render(request,'hod/course_edit.html',{'data':Course.objects.get(id = url)})

@login_required(login_url='/')
def branch_add(request):
    form = HodForms()
    if request.method == 'POST':
        fm = request.POST['name']
        if fm == "" or fm == None:
            messages.error(request,'blank input')
        else:
            form = HodForms(request.POST)
            if form.is_valid():
                branch = Branch(name = fm)
                form.instance.branch = branch
                branch.save()
                form.save()
                messages.success(request,'Branch add success')
            else:
                messages.error(request,'Something error try again')
            
            
    data = {
        'data':Branch.objects.all(),
        'fms':form
        }

    return render(request,'hod/branch_add.html',data)

@login_required(login_url='/')
def branch_edit(request,url):
    form = HodForms(instance=Hod.objects.get(branch = Branch.objects.get(id = url)))
    if request.method =='POST':
        fm = request.POST['name']
        if fm == "" or fm == None:
            messages.error(request,'Blank form Try again')
        else:
            branch =  Branch.objects.get(id = url)
            branch.name = fm
            branch.save()
            form = HodForms(request.POST,instance=Hod.objects.get(branch = Branch.objects.get(id = url)))
            form.save()
            messages.success(request,'Change success fully')

    return render(request,'hod/branch_edit.html',{'data':Branch.objects.get(id = url),'fm':form})


@login_required(login_url='/')
def branch_remove(request,url):
    Branch.objects.get(id = url).delete()
    return redirect('branch_add')


class Teacher_add(View):

    def get(self,request):
        data ={
            'branch':Branch.objects.all(),
        'course':Course.objects.all()
        }
        return render(request,'hod/teacher_add.html',data)

   
    def post(self,request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        id = request.POST.get('id')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        dob = request.POST.get('dob')
        mob = request.POST.get('mob')
        img = request.FILES.get('img',None)
        address = request.POST.get('address')
        join = request.POST.get('join')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('exp',0)
        if User.objects.filter(username = email).exists() or Teacher.objects.filter(teacher_id = id).exists():
 
            messages.error(request,f"This is User {Teacher.objects.get(teacher_id = id)} already exit   ")
       
        else:
            user = User(
                first_name = fname,
                last_name = lname,
                user_type = 2,
                username = email,
                profile_image = img,
                email = email
            )

            
            user.set_password(password)
            user.save()
            teacher = Teacher(
                admin = user,
                teacher_id = id,
                address = address,
                gender = gender,
                course = Course.objects.get(id = course),
                branch = Branch.objects.get(id = branch),
                ph = mob,
                dob = dob,
                join = join,
                qualification = qualification,
                experience = experience,
       
            )
            teacher.save()
            messages.success(request,f"User ' {email} ' Create successfully   ")
        return redirect('teacher_add')


class Teacher_list(View):


    def get(self,request):
        return render(request,'hod/teacher_list.html',{
            'data':Teacher.objects.all().order_by('-course','branch')
        })
    
    def post(self,request):
        fm = request.POST['search']
        string = fm.split()
        self.names = ''
        if fm=='' or fm == None:
            return redirect('teacher_list')
        if len(string)>1:
            print('-------------------------->',self.names)
            print(string)
            self.names = Q(first_name__icontains = string[0])|Q(last_name__icontains = string[1])
        else:
            self.names= Q(first_name__icontains = fm)|Q(last_name__icontains = fm)
        
        data = {
            'data':Teacher.objects.filter(
                Q(course__in = Course.objects.filter(name__icontains=fm))
                |Q(branch__in = Branch.objects.filter(name__icontains=fm))
                |Q(teacher_id__icontains=fm )
                |Q(ph__icontains = fm)
                |Q(admin__in=User.objects.filter(self.names))
                |Q(admin__in=User.objects.filter(email=fm))
              )
        }
        return render(request,'hod/teacher_list.html',data)

class Teacher_details(View):
    def get(self,request,url):
        data = {
            'data':Teacher.objects.get(pk = url)
        }
        return render(request,'hod/teacher_details.html',data)


class Teacher_update(View):
    def get(self,request,url):
        data = {
        'data':Teacher.objects.get(pk=url),
        'student':Student.objects.all(),
        'course':Course.objects.all(),
          'sem':Semester.objects.all(),
         'branch':Branch.objects.all(),
         'info1':User.objects.get(id = Teacher.objects.get(pk = url).admin.id)
        }
        return render(request,'hod/teacher_update.html',data)

    def post(self,request,url):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        tid = request.POST.get('tid')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        dob = request.POST.get('dob')
        mob = request.POST.get('mob')
        img = request.FILES.get('img')
        address = request.POST.get('address')
        join = request.POST.get('join')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')


       
        if 1 == '0ne':
 
            # messages.error(request,f"This is User {Teacher.objects.get(teacher_id = id)} already exit   ")
            pass
       
        else:
            user = User.objects.get(id = Teacher.objects.get(pk = url).admin.id)
            user.first_name = fname
            user.last_name = lname
            user.user_type = 2
            user.username = email
            user.email = email
            
            if not img is None or img is "":
                user.profile_image = img
            if password == None or password == "":
                user.save()
            else:
                user.set_password(password)
                user.save()

        
           
            teacher = Teacher.objects.get(pk = url)
            teacher.admin = user
            teacher.teacher_id = tid
            teacher.address = address
            teacher.gender = gender
            teacher.course = Course.objects.get(id = course)
            teacher.branch = Branch.objects.get(id = branch)
            teacher.ph = mob
            teacher.dob = dob
            teacher.join = join
            teacher.qualification = qualification
            teacher.experience = experience
       
           
            teacher.save()
            # messages.success(request,f"User ' {email} ' Update successfully   ")
        return redirect('teacher_list')



@login_required(login_url='/')
def teacher_remove(request,url):
    if request.method == 'POST':
        user = User.objects.filter(id=url)
        data = Teacher.objects.filter(admin = User.objects.get(id = url))
        data.delete()
        user.delete()
   
        return redirect('teacher_list')
        

      
    return render(request,'hod/teacher_remove.html',{'data':Teacher.objects.get(pk = url)})


@login_required(login_url='/')
def Subject_add(request):
    fm = Subject_from()
    if request.method == 'POST':

        if Subject.objects.filter(course__in=Course.objects.filter(pk = request.POST['course'])).exists() and Subject.objects.filter(branch__in=Branch.objects.filter(pk = request.POST['branch'])).exists() and Subject.objects.filter(name=request.POST['name']).exists():
            messages.warning(request,'already available..!')
        else:
            fm = Subject_from(request.POST)
            fm.save()
            messages.success(request,'course add successfully')
    return render(request,'hod/subject_add.html',{'fm':fm})


@login_required(login_url='/')
def subject_list(request):
    data = Subject.objects.all()

    return render(request,'hod/subject_list.html',{'data':data})


@login_required(login_url='/')
def subject_update(request,url):
    fm = Subject_from(instance=Subject.objects.get(id=url))
    if request.method == 'POST':
        
        if Subject.objects.get(id = url) == url and Subject.objects.filter(course__in=Course.objects.filter(pk = request.POST['course'])).exists() and Subject.objects.filter(branch__in=Branch.objects.filter(pk = request.POST['branch'])).exists() and Subject.objects.filter(name=request.POST['name']).exists():
           
            messages.warning(request,'already available..!')
        else:
            fm = Subject_from(request.POST,instance=Subject.objects.get(id=url))
            fm.save()
            messages.success(request,'course changed successfully')
    return render(request,'hod/subject_update.html',{'fm':fm})


@login_required(login_url='/')
def subject_remove(request,url):
    if request.method == 'POST':
        sub = Subject.objects.get(id=url)
        sub.delete()
        return redirect('subject_list')
    return render(request,'hod/subject_remove.html',{'data':Subject.objects.get(pk = url)})
    
 
@login_required(login_url='/')   
def session_list(request):
    fm = Session_year_form()
    if request.method == 'POST':
        if Session_year.objects.filter(session_start=request.POST['session_start']).exists() and Session_year.objects.filter(session_end=request.POST['session_end']).exists():
            messages.warning(request,'Session year already exists')
        elif(request.POST['session_start']>request.POST['session_end']):
            messages.error(request,'wrong data inputs')
        else:
            fm = Session_year_form(request.POST)
            fm.save()
            messages.success(request,'add year successfully')
        return redirect('session_list')
    return render(request,'hod/session_list.html',{'fm':fm,'data':Session_year.objects.all()})


@login_required(login_url='/')
def session_update(request,url):
    fm = Session_year_form(instance= Session_year.objects.get(id=url))
    if request.method == 'POST':
        if Session_year.objects.filter(session_start=request.POST['session_start']).exists() and Session_year.objects.filter(session_end=request.POST['session_end']).exists():
            messages.warning(request,'Session year already exists')
        elif(request.POST['session_start']>request.POST['session_end']):
            messages.error(request,'wrong data inputs')
        else:
            fm = Session_year_form(request.POST,instance= Session_year.objects.get(id=url))
            fm.save()
            messages.success(request,'changed session successfully')
        
    return render(request,'hod/session_update.html',{'fm':fm})



@login_required(login_url='/')
def session_remove(request,url):
    if request.method =='POST':
        Session_year.objects.get(id=url).delete()
        return redirect('session_list')

    return render(request,'hod/session_remove.html',{'data':Session_year.objects.get(id=url)})




class routine_add(View):
    def get(self, request):
        data = {
           'course' : Course.objects.all(),
           'branch':Branch.objects.all(),
           'sem':Semester.objects.all(),
            'subject':Subject.objects.all()
        }

        return render(request,'hod/routine_add.html',data)
    
    def post(self,request):
        
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        sem = request.POST.get('sem')

        start = request.POST.get('start')
        end = request.POST.get('end')

        monday = request.POST.get('monday')
        tuesday = request.POST.get('tuesday')
        wednesday = request.POST.get('wednesday')
        thursday = request.POST.get('thursday')
        friday = request.POST.get('friday')
        saturday = request.POST.get('saturday')
        head_routine,create = Routine_head.objects.get_or_create(branch=Branch.objects.get(id=branch),course = Course.objects.get(id=course),sem = Semester.objects.get(id=sem))
        head_routine.save()
        messages.success(request,' Routine add successfully')
        
        if request.POST.get('action') == 'true':
            routine = Routine(
                related = head_routine,
                start = start,
                end = end,
                monday = 'RECESS TIME',
                tuesday = 'RECESS TIME',
                wednesday = 'RECESS TIME',
                thursday = 'RECESS TIME',
                friday = 'RECESS TIME',
                saturday = 'RECESS TIME',

            )
            routine.save()
            messages.success(request,' Routine add successfully')

        else:
            routine = Routine(
                related = head_routine,
                start = start,
                end = end,
                monday = monday,
                tuesday = tuesday,
                wednesday = wednesday,
                thursday = thursday,
                friday = friday,
                saturday = saturday,

            )
            routine.save()

        return redirect('routine_add')


@login_required(login_url='/')
def routine_show(request):
    data = {
        'course':Routine_head.objects.all()
    }
    return render(request,'hod/routine_show.html',data)

@login_required(login_url='/')
def routine_head_update(request,url):
    fm = Routine_headForms(instance=Routine_head.objects.get(id = url))
    if request.method == "POST":
        fm = Routine_headForms(request.POST,instance=Routine_head.objects.get(id = url))
        if fm.is_valid():
            fm.save()
            messages.success(request,'Changed successfully')
        else:
            messages.error(request,'Something error try again')
    data = {
        'fm':fm
    }
    return render(request,'hod/routine_head_edit.html',data)

@login_required(login_url='/')
def routine_update(request,url,url2):
    data = {
        'data':Routine.objects.get(pk=url2),
          'course' : Course.objects.all(),
           'branch':Branch.objects.all(),
           'sem':Semester.objects.all(),
            'subject':Subject.objects.all(),
            
    }
    if request.method == 'POST':
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        sem = request.POST.get('sem')

        start = request.POST.get('start')
        end = request.POST.get('end')

        monday = request.POST.get('monday')
        tuesday = request.POST.get('tuesday')
        wednesday = request.POST.get('wednesday')
        thursday = request.POST.get('thursday')
        friday = request.POST.get('friday')
        saturday = request.POST.get('saturday')

        # if Routine.objects.filter(start=start).exists() and Routine.objects.filter(end = end).exists() and Routine_head.objects.filter(id=url).exists():
        #     messages.error(request,'In this session This time will be declared ')
        if False:
            pass
        else:
            if request.POST.get('action') == 'true':
                routine = Routine(
                    pk = url2,
                    related = Routine_head.objects.get(id=url),
                    start = start,
                    end = end,
                    monday = 'RECESS TIME',
                    tuesday = 'RECESS TIME',
                    wednesday = 'RECESS TIME',
                    thursday = 'RECESS TIME',
                    friday = 'RECESS TIME',
                    saturday = 'RECESS TIME',

                )
                routine.save()

            else:
                routine = Routine(
                    pk=url2,
                    related = Routine_head.objects.get(id=url),
                    start = start,
                    end = end,
                    monday = monday,
                    tuesday = tuesday,
                    wednesday = wednesday,
                    thursday = thursday,
                    friday = friday,
                    saturday = saturday,

                )
                routine.save()

            messages.success(request,'Successfully Updated')
    return render(request,'hod/routine_update.html',data)

def routine_remove(request,url):
    Routine.objects.get(pk=url).delete()
    return redirect('routine_show')


@login_required(login_url='/')
def notice_teacher(request):
    
    fm = Teacher_message_form()
    if request.method == 'POST':
        fm = Teacher_message_form(request.POST)
        if fm.is_valid():
            fm.save() 
            messages.success(request,'Message Sent Successfully')
     
    return render(request,'hod/notice_teacher.html',{'fm':fm})


@login_required(login_url='/')
def notice_teacher_list(request):
    data = {
        'data':Teacher_msg.objects.all()
    }
    return render(request,'hod/notice_teacher_list.html',data)


@login_required(login_url='/')
def notice_teacher_view(request,url):
    fm = Teacher_message_form(instance=Teacher_msg.objects.get(id=url))
    teacher_see = Teacher_see_msg.objects.filter(msg = Teacher_msg.objects.get(id = url))
    if request.method == 'POST':
        fm = Teacher_message_form(request.POST,instance=Teacher_msg.objects.get(id=url))
        if fm.is_valid():
            fm.save()
            messages.success(request,'Message Changed Successfully')

    return render(request,'hod/notice_teacher_view.html',{'fm':fm,'see_msg':teacher_see})


@login_required(login_url='/')
def notice_teacher_remove(request,url):
    if request.method == 'POST':
        Teacher_msg.objects.get(id=url).delete()
        return redirect('notice_teacher_list')
        
    return render(request,'hod/notice_teacher_remove.html',{'data':Teacher_msg.objects.get(id = url)})


@login_required(login_url='/')
def notice_student(request):
    fm = Student_message_form()
    if request.method == 'POST':
        fm = Student_message_form(request.POST)
        if fm.is_valid():
            fm.save() 
            messages.success(request,'Message Sent Successfully')
    return render(request,'hod/notice_student.html',{'fm':fm})


@login_required(login_url='/')
def notice_student_list(request):
     data = {
        'data':Student_msg.objects.all() 
    }
   
     return render(request,'hod/notice_student_list.html',data)

@login_required(login_url='/')
def notice_student_remove(request,url):
     Student_msg.objects.get(id=url).delete()
   
     return redirect('notice_student_list')

@login_required(login_url='/')
def notice_student_view(request,url):
    fm = Student_message_form(instance=Student_msg.objects.get(id=url))
    student_see = Student_see_msg.objects.filter(msg = Student_msg.objects.get(id = url))
    if request.method == 'POST':
        fm = Student_message_form(request.POST,instance=Student_msg.objects.get(id=url))
        
        if fm.is_valid():
            fm.save()
            messages.success(request,'Message Changed Successfully')

    return render(request,'hod/notice_student_view.html',{'fm':fm,'see_msg':student_see})


@login_required(login_url='/')
def leave_teacher(request):
    leave = teacher_leave_apply.objects.all()
    if request.method =='POST':
        inp = request.POST['filter']
        if inp == 'none':
            leave = teacher_leave_apply.objects.filter(status=None)
        elif inp == 'true':
            leave = teacher_leave_apply.objects.filter(status=True)
        elif inp == 'false':
            leave = teacher_leave_apply.objects.filter(status=False)
    data = {
        'data':leave
    }
    
    return render(request,'hod/leave_teacher.html',data)


@login_required(login_url='/')
def leave_teacher_accept(request,url):
    data = teacher_leave_apply.objects.get(id=url)
    data.status = True
    data.save()
    return redirect('leave_teacher')


@login_required(login_url='/')
def leave_teacher_reject(request,url):
    data = teacher_leave_apply.objects.get(id=url)
    data.status = False
    data.save()
    return redirect('leave_teacher')  


@login_required(login_url='/')
def leave_student(request):
    leave = Student_leave_apply.objects.all()
    if request.method =='POST':
        inp = request.POST['filter']
        if inp == 'none':
            leave = Student_leave_apply.objects.filter(status=None)
        elif inp == 'true':
            leave = Student_leave_apply.objects.filter(status=True)
        elif inp == 'false':
            leave = Student_leave_apply.objects.filter(status=False)
    data = {
        'data':leave
    }
    
    return render(request,'hod/leave_student.html',data)


@login_required(login_url='/')
def leave_student_accept(request,url):
    data = Student_leave_apply.objects.get(id=url)
    data.status = True
    data.save()
    return redirect('leave_student')

@login_required(login_url='/')
def leave_student_reject(request,url):
    data = Student_leave_apply.objects.get(id=url)
    data.status = False
    data.save()
    return redirect('leave_student')

@login_required(login_url='/')
def teacher_feedback(request):
    feedback = TeachersFeedback.objects.all()
    
    data = {
        'data' : feedback
    }
    return render(request,'hod/feedback_teacher.html',data)

@login_required(login_url='/')
def Teacher_feedback_clear(request):
    TeachersFeedback.objects.all().delete()
    return redirect('feedback_teacher')

@login_required(login_url='/')
def Teacher_feedback_delete(request,url):
    TeachersFeedback.objects.get(id =url).delete()
    return redirect('feedback_teacher')

@login_required(login_url='/')
def Teacher_feedback_replay(request,url):
    if request.method == 'POST':
        feedback = TeachersFeedback.objects.get(id =url)
        feedback.replay = request.POST.get('replay')
        feedback.status = True
        feedback.save()
        
        messages.success(request,'replay sent Successfully')
    return redirect('feedback_teacher')

@login_required(login_url='/')
def Teacher_feedback_status(request,url):
    status = TeachersFeedback.objects.get(id = url)
    status.status = True
    status.save()
    return redirect('feedback_teacher')


@login_required(login_url='/')
def student_feedback(request):
    feedback = StudentsFeedback.objects.all()
    
    data = {
        'data' : feedback
    }
    return render(request,'hod/feedback_student.html',data)

@login_required(login_url='/')
def Student_feedback_clear(request):
    StudentsFeedback.objects.all().delete()
    return redirect('feedback_student')


@login_required(login_url='/')
def student_feedback_status(request,url):
    status = StudentsFeedback.objects.get(id = url)
    status.status = True
    status.save()
    return redirect('feedback_student')

@login_required(login_url='/')
def student_feedback_replay(request,url):
    if request.method == 'POST':
        feedback = StudentsFeedback.objects.get(id =url)
        feedback.replay = request.POST.get('replay')
        feedback.status = True
        feedback.save()
        
        messages.success(request,'replay sent Successfully')
    return redirect('feedback_student')


@login_required(login_url='/')
def student_feedback_delete(request,url):
    StudentsFeedback.objects.get(id =url).delete()
    return redirect('feedback_student')

@login_required(login_url='/')
def hostel_add(request):
    if request.method == "POST":
        block = request.POST.get('block')
        room = request.POST.get('room')
        bed = request.POST.get('bed')
        cost = request.POST.get('cost')
        hostel = Hostel(
          block = block,
          room = room,
          no_of_bed = bed,
          cost = cost
        )
        hostel.save()
        messages.success(request,'successfully room added')
    return render(request,'hod/hostel_add.html')

@login_required(login_url='/')
def hostel_list(request):
    data = {
        'data':Hostel.objects.all().order_by('-id')
    }
    return render(request,'hod/hostel_list.html',data)

@login_required(login_url='/')
def hostel_details(request,url):
    
    if request.method == 'POST':
        block = request.POST.get('block')
        room = request.POST.get('room')
        bed = request.POST.get('bed')
        cost = request.POST.get('cost')
        student = request.POST.get('student')

        data = Hostel.objects.get(id=url)
        data.block = block
        data.room = room
        data.no_of_bed = bed
        data.cost = cost
        
       
        
        data.save()
        messages.success(request,'Hostel data changed successfully')

        if student != "":
            try:
                student_condition = Student.objects.filter(admin = User.objects.get(username = student)).exists()
                if student_condition:
                    
                    try:
                        Hostel_student.objects.filter(student = Student.objects.get(admin = User.objects.get(username = student))).exists()
                        data = Hostel_student.objects.get(student = Student.objects.get(admin = User.objects.get(username = student))).hostel.room
                        messages.warning(request,f'already exist , room no is <b>{data}</b> ')
                    except:
                        Hostel_student(
                            hostel = Hostel.objects.get(id=url),
                            student = Student.objects.get(admin = User.objects.get(username = student ))
                        ).save()
                        messages.success(request,'Student admission successfully')
            #        
            except:
                messages.error(request,f'Reg ( <b>{student}</b> ) not found try again !')
        # else:
        #     
    data = Hostel.objects.get(id=url)
    if int(Hostel.objects.get(id=url).no_of_bed) == int(len(Hostel_student.objects.filter(hostel =Hostel.objects.get(id=url)))):
            data.available = True
            data.save()
    else:
        data.available = False
        print('------------------------>>',int(len(Hostel_student.objects.filter(hostel =Hostel.objects.get(id=url)))))
        data.available_bed = int(Hostel.objects.get(id=url).no_of_bed)-int(len(Hostel_student.objects.filter(hostel =Hostel.objects.get(id=url))))
        data.save()
        
    data = {
        'data':Hostel.objects.get(id=url),
        'student':Hostel_student.objects.filter(hostel = Hostel.objects.get(id=url)).order_by('-id')
    }
    return render(request,'hod/hostel_details.html',data)

@login_required(login_url='/')
def hostel_remove(request,url):
    Hostel.objects.get(id = url).delete()
    return redirect('hostel_list')

@login_required(login_url='/')
def hostel_student_remove(request,url):
    student = Hostel_student.objects.get(student = Student.objects.get(admin = User.objects.get(id = url)))
    student.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/')
def transport_add(request):
    fm = Transport_form()
    if request.method == 'POST':
        fm = Transport_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Transport add successfully')
        else:
            messages.error(request,'Something error please try again')
    return render(request,'hod/transport_add.html',{'fm':fm})

@login_required(login_url='/')
def transport_list(request):
    data = {
        'data':Transport.objects.all().order_by('-id')
    }
    return render(request,'hod/transport_list.html',data)

@login_required(login_url='/')
def transport_edit(request,url):
    data = Transport.objects.get(id = url)
    fm = Transport_form(instance=data)

    if request.method == 'POST':
        fm = Transport_form(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Transport changed successfully')
        else:
            messages.success(request,'Something error please try again ')

    return render(request,'hod/transport_edit.html',{'fm':fm,'data':data})


@login_required(login_url='/')
def transport_remove(request,url):
    data = Transport.objects.get(id = url)
    data.delete()
    return redirect('transport_list')

def quiz_list(request):
    data = {
        'data':Quiz.objects.all().order_by('-id')
     }

    return render(request,'hod/quiz_list.html',data)

def quiz_view(request,url):
    quiz = Quiz.objects.get(pk = url)
    data = {
        'data':Quiz_result.objects.filter(quiz = quiz)
    }
    return render(request,'hod/quiz_view.html',data)


def assignment_list(request):  
    data = {
        'data':Assignment.objects.all().order_by('-id')
    }
    return render(request,'hod/assignment_list.html',data)

def assignment_view(request,url):
    data = {
        'data':Assignment_submit_student.objects.filter(assignment = Assignment.objects.get(id = url)),
        'head':Assignment.objects.get(id = url)
    }
    return render(request,'hod/assignment_view.html',data)

def setting(request):
    sem = Semester.objects.all()
    course = Course.objects.all()
        
    data = {
        'sem':sem,
        'course':course
    }
    return render(request,'hod/setting.html',data)

def changed_branch(request):
    if request.method == "POST":
        current_sem = request.POST.get('current_sem')
        update_sem = request.POST.get('update_sem')
        post_data = request.POST.get('course_set_for_sem')
        if post_data != "no":
            course = Course.objects.get(id = post_data).pk
  
            Student.objects.filter(semester = current_sem,course = course).update(semester = update_sem)
            messages.success(request,'Branch change successfully')
        else:
            messages.warning(request,'please Fill up the course')
    return redirect('hod_setting')

def setting_remove__last_year_student(request):
      course = request.POST.get('course')
      sem = request.POST.get('sem')
      data  = Student.objects.filter(course = Course.objects.get(id = course),semester = Semester.objects.get(id = sem))
      data.delete()
      messages.success(request,'Successfully last year student data remove.!')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))