from django.shortcuts import render,redirect
from django.http import HttpResponse
from server.models import *
from server.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required(login_url='/')
def home(request):
    gender = Teacher.objects.get(admin = User.objects.get(id = request.user.id))
    user = Teacher_see_msg.objects.filter(teacher = Teacher.objects.get(admin = User.objects.get(id = request.user.id)))
    teacher = Teacher.objects.filter(branch=Teacher.objects.get(admin = request.user).branch,course = Teacher.objects.get(admin = request.user).course)
    student = Student.objects.filter(branch=Teacher.objects.get(admin = request.user).branch,course = Teacher.objects.get(admin = request.user).course)
    quiz = Quiz.objects.filter(name = Teacher.objects.get(admin = request.user))
    assignment=Assignment.objects.filter(teacher = Teacher.objects.get(admin = request.user))
    fm = Notice_teacher_to_student_Form()
    if request.method == 'POST':
        fm = Notice_teacher_to_student_Form(request.POST,request.FILES)
        if fm.is_valid():
            fm.instance.teacher = Teacher.objects.get(admin = request.user)
            fm.save()
            messages.success(request,'Notice sent successful')
        else:
            messages.warning(request,'Please enter valid data')
    
    notice_list = Notice_teacher_to_student.objects.filter(teacher = Teacher.objects.get(admin = request.user)).order_by('-id')
    data = {
        'gen':gender,
        'condition':len(user) != len(Teacher_msg.objects.all()),
        'fm':fm,
        'notice_list':notice_list,
        'teacher_count':teacher.count(),
        'student_count':student.count(),
        'quiz_count':quiz.count(),
        'assignment_count':assignment.count()
    }
    return render(request,'teacher/home.html',data)

@login_required(login_url='/')
def hod_notify(request):
    data = {
      'data':Teacher_msg.objects.all().order_by('-date')
    }
    return render(request,'teacher/hod_notify.html',data)

@login_required(login_url='/')
def hod_notify_show(request,url):
    msg = Teacher_msg.objects.get(id = url)
    user = Teacher.objects.get(admin = request.user)
    notify,see_notify = Teacher_see_msg.objects.get_or_create(msg = msg,teacher = user)
    notify.save()

    data = {
        'data':Teacher_msg.objects.get(id = url),
       

    }
    return render(request,'teacher/hod_notify_show.html',data)

@login_required(login_url='/')
def leave_apply(request):
    fm = teacher_leave_apply_form()
    u_id = Teacher.objects.get(admin = User.objects.get(id = request.user.id))
    
    data ={
        'fm':fm,
        'user_id' : u_id
    }
    if request.method == 'POST':
        fm = teacher_leave_apply_form(request.POST)
        if fm.is_valid():
            fm.instance.user_id = u_id
            fm.save()
            messages.success(request,'Leave apply successfully')
        else:
            messages.error(request,'Something error try again !')
    return render(request,'teacher/leave_apply.html',data)

@login_required(login_url='/')
def leave_list(request):
    leave = teacher_leave_apply.objects.filter(user_id=Teacher.objects.get(admin = User.objects.get(id=request.user.id)))
    if request.method =='POST':
        inp = request.POST['filter']
        if inp == 'none':
            leave = teacher_leave_apply.objects.filter(status=None,user_id=Teacher.objects.get(admin = User.objects.get(id=request.user.id)))
        elif inp == 'true':
            leave = teacher_leave_apply.objects.filter(status=True,user_id=Teacher.objects.get(admin = User.objects.get(id=request.user.id)))
        elif inp == 'false':
            leave = teacher_leave_apply.objects.filter(status=False,user_id=Teacher.objects.get(admin = User.objects.get(id=request.user.id)))
    data = {
        'data':leave
    }
    return render(request,'teacher/leave_list.html',data)

@login_required(login_url='/')
def leave_list_remove(request,url):
    teacher_leave_apply.objects.get(id=url).delete()
    return redirect('teacher_leave_list')

@login_required(login_url='/')
def view_leave(request,url):
    u_leave = teacher_leave_apply.objects.get(id = url)
    fm = teacher_leave_apply_form(instance=u_leave)
    if request.method == 'POST':
        fm = teacher_leave_apply_form(request.POST,instance=u_leave)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Changed successfully')
        else:
            messages.error(request,'something want wrong please input valid data')
    data = {
        'fm':fm,
        'data':u_leave
    }
    return render(request,'teacher/view_leave.html',data)


@login_required(login_url='/')
def feedback(request):
    fm = Teacher_feedback_form()
    if request.method == 'POST':
        fm = Teacher_feedback_form(request.POST)
        if fm.is_valid():
            fm.instance.user_id = Teacher.objects.get(admin = User.objects.get(id = request.user.id))
            fm.save()
            messages.success(request,'Feedback sent successfully')
        else:
            messages.error(request,'Something want wrong try again !')
    data = {
        'fm':fm
    }
    return render(request,'teacher/feedback.html',data)


@login_required(login_url='/')
def  feedback_list(request):
    feedback_list =  TeachersFeedback.objects.filter(user_id = Teacher.objects.get(admin = User.objects.get(id = request.user.id)))
    data = {
        'data':feedback_list
    }
    return render(request,'teacher/feedback_list.html',data)


@login_required(login_url='/')
def feedback_remove(request,url):
    TeachersFeedback.objects.get(id=url).delete()
    return redirect('teacher_feedback_list')


@login_required(login_url='/')
def feedback_view(request,url):
    fm = Teacher_feedback_form(instance=TeachersFeedback.objects.get(id = url))
    if request.method == 'POST':
        fm = Teacher_feedback_form(request.POST,instance=TeachersFeedback.objects.get(id = url))
        fm.save()
        messages.success(request,'Feedback hanged Successfully')
    data = {
        'fm':fm,
        'data':TeachersFeedback.objects.get(id = url)
    }
    return render(request,'teacher/feedback_view.html',data)

@login_required(login_url='/')
def take_attendance(request):
    sub = Subject.objects.filter(teacher = Teacher.objects.get(admin = User.objects.get(id = request.user.id)))
    sem =  Semester.objects.all()
    
    data = {
        'sub':sub,
        'sem':sem
    }
    return render(request,'teacher/attendance_take.html',data)

@login_required(login_url='/')
def attendance_search_student(request,branch,course,sub,sem):
    stu = Student.objects.filter(branch=Branch.objects.get(id = branch),course = Course.objects.get(id=course),semester = Semester.objects.get(id = sem))
    if request.method == 'POST':
        date = request.POST.get('date')
        
        student_list = request.POST.getlist('student_status')
        if Attendance.objects.filter( subject = Subject.objects.get(id = sub),teacher = Teacher.objects.get(admin = User.objects.get(id = request.user.id)),date = date).exists():
            messages.warning(request,'already attendance taken,View and edit as for requirement')
        else:
            attendance = Attendance(
                subject = Subject.objects.get(id = sub),
                teacher = Teacher.objects.get(admin = User.objects.get(id = request.user.id)),
                date = date
            )

            attendance.save()
            messages.success(request,'attendance take successfully')
            for i in student_list:
                Attendance_chields(
                student =  Student.objects.get(admin = User.objects.get(id = int(i))),
                attendance = attendance,
                date = date,
                subject = Subject.objects.get(id = sub)
                ).save()
         
    data = {
        'data':stu
    }
    return render(request,'teacher/attendance_search_student.html',data)

@login_required(login_url='/')
def attendance_show(request,sub):
    sub = Subject.objects.get(id = sub)
    data = {
        'data':Attendance.objects.filter(subject = sub,teacher = Teacher.objects.get(admin = User.objects.get(id = request.user.id))).order_by('-id'),
        
    }
    return render(request,'teacher/attendance_show.html',data)

@login_required(login_url='/')
def online_class(request):
    fm = Online_classForm()
    if request.method == 'POST':
        sub = request.POST.get('sub')
        if sub != "" or sub !=None:
            fm = Online_classForm(request.POST)
            if fm.is_valid:
                fm.instance.subject = Subject.objects.get(id = sub)
                fm.instance.user= Teacher.objects.get(admin= request.user)
               
                fm.save()
                messages.success(request,'Online class added successful ')
            else:
                messages.error(request,'Something error try again !')
        else:
            messages.warning(request,'Please select the subject')
            
    data = {
        'fm':fm,
        'sub':Subject.objects.filter(teacher = Teacher.objects.get(admin = request.user))
    }
    return render(request,'teacher/online_class.html',data)

@login_required(login_url='/')
def online_class_list(request):
    data  = Student_online_class.objects.filter(user = Teacher.objects.get(admin= request.user)).order_by('-id')
    return render(request,'teacher/online_class_list.html',{'data':data})

@login_required(login_url='/')
def online_class_view(request,url):
    data =Student_online_class.objects.get(id = url)
    fm = Online_classForm(instance=data)
    sub=Subject.objects.filter(teacher = Teacher.objects.get(admin = request.user))
    if request.method == 'POST':
        fm = Online_classForm(request.POST,instance=Student_online_class.objects.get(id = url))
        if fm.is_valid():
            fm.save()
            messages.success(request,'Update class Successfully')
        else:
            messages.error(request,'Something error happened try again')
    return render(request,'teacher/online_class_view.html',{'fm':fm,'sub':sub,'data':data})

@login_required(login_url='/')
def online_class_remove(request,url):
    data =Student_online_class.objects.get(id = url)
    data.delete()
    return redirect('online_class_list')


@login_required(login_url='/')
def quiz_add(request):
    if request.method == 'POST':
        fm = Quiz_form(request.POST)
        if fm.is_valid():
            fm.instance.name = Teacher.objects.get(admin = request.user)
            fm.save()
            return redirect('quiz_list')
        else:
            messages.error(request,'something error try again !')
            return redirect('quiz_add')
    data = {
        'fm': Quiz_form()
        }
    return render(request,'teacher/quiz_add.html',data)

    
@login_required(login_url='/')
def quiz_qn_add(request,url):
    if request.method == 'POST':
        Question_Input = request.POST.getlist('ans')
        Question_correct_choice1 = request.POST.get('check_inp1')
        Question_correct_choice2 = request.POST.get('check_inp2')
        Question_correct_choice3 = request.POST.get('check_inp3')
        Question_correct_choice4 = request.POST.get('check_inp4')
        if Question_correct_choice1 is None and Question_correct_choice2 is None and Question_correct_choice3 is None and Question_correct_choice4 is None:
            messages.error(request,'Please select the correct answer')
        else:

            qn_text = request.POST.get('text')
            qn_fm = Quiz_qn(
            text = qn_text,
            quiz = Quiz.objects.get(id = url)
            )
            qn_fm.save()
                #  4 ans Part...
            checkBoxList = [Question_correct_choice1,Question_correct_choice2,Question_correct_choice3,Question_correct_choice4]
            for i in range(len(Question_Input)):
                if checkBoxList[i] != 'on':
                    Quiz_ans(
                        text = Question_Input[i],
                        correct = False,
                        question = qn_fm
                    ).save()
                else:
                    Quiz_ans(
                        text = Question_Input[i],
                        correct = True,
                        question = qn_fm
                    ).save()
            
    data = {
        'data': Quiz_qn.objects.filter(quiz = Quiz.objects.get(id = url)).order_by('-id'),
        'qn_fm':Quiz_qn_form(),
        'count_condition':int(Quiz.objects.get(id = url).num_of_qn) <= len(Quiz_qn.objects.filter(quiz = Quiz.objects.get(id = url)))
     }

    return render(request,'teacher/quiz_qn_add.html',data)

           
            

@login_required(login_url='/')
def quiz_list(request):
    data = {
        'data':Quiz.objects.filter(name = Teacher.objects.get(admin = request.user)).order_by('-id')
    }
    return render(request,'teacher/quiz_list.html',data)

@login_required(login_url='/')
def quiz_edit(request,url):
    quiz = Quiz.objects.get(id = url)
    if request.method == 'POST':
        quiz_fm = Quiz_form(request.POST,instance = quiz)
        if quiz_fm.is_valid():
            quiz_fm.save()
            messages.success(request,'Successfully Quiz edit')
        else:
            messages.error(request,'Please input valid data')
    data={
        'fm':Quiz_form(instance = quiz)
    }
    return render(request,'teacher/quiz_edit.html',data)
        
@login_required(login_url='/')      
def quiz_delete(request,url):
    Quiz.objects.get(id = url).delete()
    messages.warning(request,'Remove data Quiz successful ')
    return redirect('quiz_list')

@login_required(login_url='/')
def quiz_qn_view(request,url):
    quiz_qn = Quiz_qn.objects.get(id = url)
    quiz_strength = quiz_qn.quiz.num_of_qn
    if request.method == 'POST':
        Question_Input = request.POST.getlist('ans')
        Question_correct_choice1 = request.POST.get('check_inp1')
        Question_correct_choice2 = request.POST.get('check_inp2')
        Question_correct_choice3 = request.POST.get('check_inp3')
        Question_correct_choice4 = request.POST.get('check_inp4')

        qn_fm = Quiz_qn_form(request.POST,instance = quiz_qn)
        qn_fm.save()
            #  4 ans Part...
        checkBoxList = [Question_correct_choice1,Question_correct_choice2,Question_correct_choice3,Question_correct_choice4]
        old_answer_input =  Quiz_ans.objects.filter(question = quiz_qn)
        if Question_correct_choice1 is None and Question_correct_choice2 is None and Question_correct_choice3 is None and Question_correct_choice4 is None:
            for i in range(len(old_answer_input)):
                old_answer_input[i].text = Question_Input[i]
                old_answer_input[i].question = quiz_qn
                old_answer_input[i].correct = old_answer_input[i].correct
                old_answer_input[i].save() 
            
           
        else:
         for i in range(len(old_answer_input)):
            old_answer_input[i].text = Question_Input[i]
            old_answer_input[i].question = quiz_qn
            if checkBoxList[i] == 'on':
                old_answer_input[i].correct = True
                old_answer_input[i].save()   
            else:  
                old_answer_input[i].correct = False
                old_answer_input[i].save()
        messages.success(request,'Changed successful') 
                
    data = {
        'qn_fm':Quiz_qn_form(instance = quiz_qn),
        'data':quiz_qn,
        
    }
    return render(request,'teacher/quiz_qn_view.html',data)
   

@login_required(login_url='/')
def quiz_qn_delete(request,url):
    Quiz_qn.objects.get(pk = url).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
@login_required(login_url='/')
def quiz_result_view(request,url):
    quiz = Quiz.objects.get(pk = url)
    data = {
        'data':Quiz_result.objects.filter(quiz = quiz)
    }
    return render(request,'teacher/quiz_result_view.html',data)

@login_required(login_url='/')
def assignment_create(request):
    fm = Assignment_create_form()
    if request.method == 'POST':
        fm = Assignment_create_form(request.POST)
        online = request.POST.get('online')
        offline = request.POST.get('offline')
        if online == None and offline == None:
            messages.error(request,'Choose online or offline assignment Submit!')
        else:
            if fm.is_valid():
                fm.instance.teacher = Teacher.objects.get(admin = request.user)
                fm.save()
                messages.success(request,'Assignment add successful.!')
          
    data = {
        'fm':fm
    }
    return render(request,'teacher/assignment_create.html',data)
  
         
def assignment_list(request):
    
    data = {
        'data':Assignment.objects.filter(teacher = Teacher.objects.get(admin = request.user)).order_by('-id')
    }
    return render(request,'teacher/assignment_list.html',data)


def assignment_edit(request,url):
    fm = Assignment_create_form(instance=Assignment.objects.get(id = url))
    if request.method == 'POST':
        fm = Assignment_create_form(request.POST,instance=Assignment.objects.get(id = url))
        if fm.is_valid():
            fm.save()
            messages.success(request,'Assignment Edit Successful')
        else:
            messages.error(request,'input the valid Data')

    data = {
        'fm':fm
    }
    return render(request,'teacher/assignment_edit.html',data)

def assignment_remove(request,url):
    Assignment.objects.get(id = url).delete()
    messages.error(request,'Assignment Remove successful')
    return redirect('teacher_assignment_list')

def assignment_view(request,url):
    assignment_student_data = Assignment_submit_student.objects.filter(assignment = Assignment.objects.get(id = url))

    fm = Assignment_resultForm()

    data = {
        'data':assignment_student_data,
        'fm':fm
    }
    return render(request,'teacher/assignment_view.html',data)

def assignment_result(request):

    if Assignment_result.objects.filter(assignment = Assignment_submit_student.objects.get(id = request.POST.get('assignment'))).exists():
        ass = Assignment_submit_student.objects.get(id = request.POST.get('assignment'))
        teacher_accept = request.POST.get('teacher_accept')
        def teacher_accept_condition(data):
            if data == 'true':
                return True
            else:
                return False
        teacher_mark = request.POST.get('teacher_mark')
        assignment_res = Assignment_result.objects.get(assignment = ass)
        assignment_res.assignment = ass
        assignment_res.teacher_accept = teacher_accept_condition(teacher_accept)
        assignment_res.teacher_mark = teacher_mark
        assignment_res.save()
        messages.success(request,'Successfully changed')
    else:
        fm = Assignment_resultForm(request.POST)
        if fm.is_valid():
            fm.instance.assignment = Assignment_submit_student.objects.get(id = request.POST.get('assignment') )
            fm.save()
            messages.success(request,'Mark given successFull')
        else:
            messages.error(request,'something error try again')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def star_student(request):
    if request.method == 'POST':
        try:
            reg = Student.objects.get(admin = User.objects.get(username = request.POST.get('reg_inp')))
        except:
            messages.error(request,"reg no doesn't exits")
            return redirect('teacher_star_student')
        user = Teacher.objects.get(admin =request.user)
        if StarStudent.objects.filter(user=reg).exists():
            messages.warning(request,'User already exits')
            return redirect('teacher_star_student')
        else:
            model_data = StarStudent(user=reg,hod = user)
            model_data.save()
            messages.success(request,'User add successfully')
    
    course = Teacher.objects.get(admin =request.user).course
    branch = Teacher.objects.get(admin =request.user).branch
    student = Student.objects.filter(course = course,branch = branch)
    data = {
       'data': StarStudent.objects.all(),
       'branch':StarStudent.objects.filter(user__in = student)
    }
    return render(request,'teacher/star_student.html',data)

def star_student_remove(request,url):
    StarStudent.objects.get(id = url).delete()
    messages.success(request,'Remove Star Student')
    return redirect('teacher_star_student')

def notice_to_student_remove(request,url):
    Notice_teacher_to_student.objects.get(id = url).delete()
    return redirect('teacher_home')