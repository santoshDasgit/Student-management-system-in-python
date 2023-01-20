from django.shortcuts import render,redirect
from django.http import HttpResponse
from server.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from server.forms import *
from server.templatetags import simpletag

@login_required(login_url='/')
def home(request):
    
    user = Student_see_msg.objects.filter(student = Student.objects.get(admin = User.objects.get(id = request.user.id)))
    sub  = Subject.objects.filter(branch=Student.objects.get(admin = request.user).branch,course = Student.objects.get(admin = request.user).course,sem = Student.objects.get(admin = request.user).semester )
    attendance = Attendance.objects.filter(subject__in = sub).count()
    teacher = Teacher.objects.filter(branch=Student.objects.get(admin = request.user).branch,course = Student.objects.get(admin = request.user).course)
    quizs = Quiz.objects.filter(branch=Student.objects.get(admin = request.user).branch,course = Student.objects.get(admin = request.user).course,sem = Student.objects.get(admin = request.user).semester)
    assignment = Assignment.objects.filter(subject__in = sub)
    star_student = StarStudent.objects.all()
    notice_to_teacher = Notice_teacher_to_student.objects.filter(branch=Student.objects.get(admin = request.user).branch,course = Student.objects.get(admin = request.user).course,sem = Student.objects.get(admin = request.user).semester)
    data = {
        
        'condition':len(user) != len(Student_msg.objects.all()),
        'attendance': attendance,
        'teacher':teacher.count(), 
        'quiz':quizs.count(),
        'assignment':assignment.count(),
        'star_student':star_student,
        'notice_to_teacher':notice_to_teacher
    }
    return render(request,'student/home.html',data)


@login_required(login_url='/')
def student_notify(request):
    data = {
      'data':Student_msg.objects.all().order_by('-date')
    }
    return render(request,'student/hod_notify.html',data)

@login_required(login_url='/')
def student_notify_show(request,url):
    
    msg = Student_msg.objects.get(id = url)
    user = Student.objects.get(admin = request.user)
    notify,see_notify = Student_see_msg.objects.get_or_create(msg = msg,student = user)
    notify.save()

    data = {
            'data':Student_msg.objects.get(id = url),
    }

    return render(request,'student/hod_notify_show.html',data)


@login_required(login_url='/')
def leave_apply(request):
    fm = student_leave_apply_form()
    u_id = Student.objects.get(admin = User.objects.get(id = request.user.id))
    
    data ={
        'fm':fm,
        'user_id' : u_id
    }
    if request.method == 'POST':
        fm = student_leave_apply_form(request.POST)
        if fm.is_valid():
            fm.instance.user_id = u_id
            fm.save()
            messages.success(request,'Leave apply successfully')
        else:
            messages.error(request,'Something error try again !')
    return render(request,'student/leave_apply.html',data)

@login_required(login_url='/')
def leave_list(request):
    leave = Student_leave_apply.objects.filter(user_id=Student.objects.get(admin = User.objects.get(id=request.user.id)))
    if request.method =='POST':
        inp = request.POST['filter']
        if inp == 'none':
            leave = Student_leave_apply.objects.filter(status=None,user_id=Student.objects.get(admin = User.objects.get(id=request.user.id)))
        elif inp == 'true':
            leave = Student_leave_apply.objects.filter(status=True,user_id=Student.objects.get(admin = User.objects.get(id=request.user.id)))
        elif inp == 'false':
            leave = Student_leave_apply.objects.filter(status=False,user_id=Student.objects.get(admin = User.objects.get(id=request.user.id)))
    data = {
        'data':leave
    }
    return render(request,'student/leave_list.html',data)
   

@login_required(login_url='/')
def leave_list_remove(request,url):
    Student_leave_apply.objects.get(id=url).delete()
    return redirect('student_leave_list')
    
    

@login_required(login_url='/')
def view_leave(request,url):
    u_leave = Student_leave_apply.objects.get(id = url)
    fm = student_leave_apply_form(instance=u_leave)
    if request.method == 'POST':
        fm = student_leave_apply_form(request.POST,instance=u_leave)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Changed successfully')
        else:
            messages.error(request,'something want wrong please input valid data')
    data = {
        'fm':fm,
        'data':u_leave
    }
    return render(request,'student/view_leave.html',data)


@login_required(login_url='/')
def feedback(request):
    fm = Student_feedback_form()
    if request.method == 'POST':
        fm = Student_feedback_form(request.POST)
        if fm.is_valid():
            fm.instance.user_id = Student.objects.get(admin = User.objects.get(id = request.user.id))
            fm.save()
            messages.success(request,'Feedback sent successfully')
        else:
            messages.error(request,'Something want wrong try again !')
    data = {
        'fm':fm
    }
    return render(request,'student/feedback.html',data)

@login_required(login_url='/')
def  feedback_list(request):
    feedback_list =  StudentsFeedback.objects.filter(user_id = Student.objects.get(admin = User.objects.get(id = request.user.id)))
    data = {
        'data':feedback_list
    }
    return render(request,'student/feedback_list.html',data)


@login_required(login_url='/')
def feedback_remove(request,url):
    StudentsFeedback.objects.get(id=url).delete()
    return redirect('student_feedback_list')

@login_required(login_url='/')
def feedback_view(request,url):
    fm = Student_feedback_form(instance=StudentsFeedback.objects.get(id = url))
    if request.method == 'POST':
        fm = Student_feedback_form(request.POST,instance=StudentsFeedback.objects.get(id = url))
        fm.save()
        messages.success(request,'Feedback hanged Successfully')
    data = {
        'fm':fm,
        'data':StudentsFeedback.objects.get(id = url)
    }
    return render(request,'student/feedback_view.html',data)

@login_required(login_url='/')
def routine(request):
    return render(request,'')
    
@login_required(login_url='/')
def routine(request):
    course = Student.objects.get(admin = User.objects.get(id = request.user.id)).course
    branch = Student.objects.get(admin = User.objects.get(id = request.user.id)).branch
    sem = Student.objects.get(admin = User.objects.get(id = request.user.id)).semester
    data = {
        'course':Routine_head.objects.filter(course = course,branch=branch,sem = sem)
    }
    return render(request,'student/routine.html',data)

@login_required(login_url='/')
def Teacher_details(request,url):
    
    data = {
            'data':Teacher.objects.get(pk = url)
    }
    return render(request,'student/teacher_details.html',data)

@login_required(login_url='/')
def student_see_attendance(request):
    sub = Subject.objects.filter(branch=Student.objects.get(admin = request.user).branch,course = Student.objects.get(admin = request.user).course)
    data = {
        'sub':sub
    }
    return render(request,'student/attendance.html',data)

@login_required(login_url='/')
def online_class(request):
    data = Student_online_class.objects.all().order_by('-id')

    return render(request,'student/online_class.html',{'data':data,'student':Student.objects.get(admin = request.user)})

@login_required(login_url='/')
def group_discuss(request):
    data = {
        'replay_gd':Gd_replay_form(),
        'data':Group_discussion.objects.filter(
        user_type = request.user.user_type,
        course= Course.objects.get(id = Student.objects.get(admin = request.user).course.pk),
        branch= Branch.objects.get(id = Student.objects.get(admin = request.user).branch.pk),
        sem= Semester.objects.get(id = Student.objects.get(admin = request.user).semester.pk)
        )
    }
    return render(request,'student/gd_list.html',data)

@login_required(login_url='/')
def group_discuss_add(request):
    fm = Gd_form()
    if request.method == 'POST':
        fm = Gd_form(request.POST,request.FILES)
        text = request.POST.get('text')
        image = request.POST.get('image')

        if fm.is_valid():
            fm.instance.user = Student.objects.get(admin = request.user)
            fm.instance.user_type = request.user.user_type
            fm.instance.course = Student.objects.get(admin = request.user).course
            fm.instance.branch = Student.objects.get(admin = request.user).branch
            fm.instance.sem = Student.objects.get(admin = request.user).semester
            if text == "" and image == "":
                return redirect('student_group_discuss')
            else:
                fm.save()
                return redirect('student_group_discuss')
        else:
            messages.error(request,'Something error try again')
            
    data = {
        'fm':fm
    }
    return render(request,'student/gd_add.html',data)


@login_required(login_url='/')
def group_discuss_replays(request,url):
    if request.method == 'POST':
        fm = Gd_replay_form(request.POST,request.FILES)
        text = request.POST.get('text')
        image = request.POST.get('image')
        if fm.is_valid():
            fm.instance.gd = Group_discussion.objects.get(id = url)
            fm.instance.user = Student.objects.get(admin = request.user)
            if text == "" and image == "":
                return redirect('student_group_discuss')
            else:
                fm.save()
                return redirect('student_group_discuss')
        else:
            pass

@login_required(login_url='/')
def group_discuss_remove(request,url):
    Group_discussion.objects.get(id=url).delete()
    return redirect('student_group_discuss')


@login_required(login_url='/')
def group_discuss_replay_remove(request,url):
    Group_discussion_replay.objects.get(id=url).delete()
    return redirect('student_group_discuss')

@login_required(login_url='/')
def quiz(request):
    course = Student.objects.get(admin = request.user).course
    branch = Student.objects.get(admin = request.user).branch
    sem = Student.objects.get(admin = request.user).semester
    data = {
        'data':Quiz.objects.filter(course = course,branch = branch, sem = sem),
        'result':Quiz_result.objects.filter(user = Student.objects.get(admin = request.user))
    }
   
    return render(request,'student/quiz_list.html',data)

def quiz_qn_test(request,url):
    quiz = Quiz.objects.get(id=url)
    quiz_id = Quiz_qn.objects.filter(quiz = quiz)
    count_mark = 0
    try:
        Quiz_result.objects.get( quiz = quiz,
        user = Student.objects.get(admin = request.user))
        return redirect('student_quiz_end_page')
    except:
        if request.method == "POST":
            for i in quiz_id:
                radio_data = request.POST.get(f'check_inp{i.pk}')
                if radio_data is None:
                    count_mark = count_mark
                else:
                    ans = Quiz_ans.objects.get(id = radio_data)
                    if ans.correct:
                        count_mark +=1
                    else:
                        count_mark = count_mark
            
            quiz_res = Quiz_result(
                quiz = quiz,
                user = Student.objects.get(admin = request.user),
                total_mark = count_mark,
                score = count_mark/len(quiz_id) * 100
                )
            pass_or_fell = simpletag.quiz_pass_fell(count_mark/len(quiz_id) * 100,quiz.pass_mark)
            quiz_res.result_status = pass_or_fell
            quiz_res.save()
            return redirect('student_quiz_end_page')
                
            

        
            
            

    data = {
      'data' : Quiz_qn.objects.filter(quiz = quiz).order_by('-id'),
      'quiz_details':Quiz.objects.get(id=url),
     
    }
    return render(request,'student/quiz_qn.html',data)


def quiz_end_page(request):
    return render(request,'student/quiz_end.html')

def quiz_view_page(request,url):
    data = {
        'data': Quiz_qn.objects.filter(quiz = Quiz.objects.get(id = url)).order_by('-id'),
        'count_condition':int(Quiz.objects.get(id = url).num_of_qn) <= len(Quiz_qn.objects.filter(quiz = Quiz.objects.get(id = url)))
     }
    return render(request,'student/quiz_view.html',data)

def assignment_list(request):
    branch = Student.objects.get(admin = request.user).branch
    course = Student.objects.get(admin = request.user).course
    sem = Student.objects.get(admin = request.user).semester
    sub = Subject.objects.filter(course=course,branch=branch,sem=sem)
    assignment = Assignment.objects.filter(subject__in = sub,assignment_start=True)
    data = {
        'data':assignment
    }
    return render(request,'student/assignment_list.html',data)

def assignment_view(request,url):
    fm = Assignment_upload_student_form()
    if request.method == 'POST':
        fm = Assignment_upload_student_form(request.POST,request.FILES)
        file = request.POST.get('file')
        offline = request.POST.get('offline')
        if file is '' and offline is None:
            messages.error(request,'please select offline or online')
        else:
            if Assignment_submit_student.objects.filter(assignment = Assignment.objects.get(id = url),student = Student.objects.get(admin = request.user)).exists():
                messages.warning(request,'already your  record is submitted you can edit!')
            else:
                if fm.is_valid():
                    fm.instance.assignment = Assignment.objects.get(id = url)
                    fm.instance.student = Student.objects.get(admin = request.user)
                    fm.save()
                    messages.success(request,'Respond submitted successful')
    data = {
        'fm':fm
    }
    return render(request,'student/assignment_view.html',data)

def assignment_edit(request,url):
    assignment = Assignment.objects.get(id = url)
    try:
        fm = Assignment_upload_student_form(instance= Assignment_submit_student.objects.get(assignment = assignment,student = Student.objects.get(admin = request.user)))
    except:

        messages.error(request,"Something error try again")
        return redirect('student_assignment_list')
    cheak_data = Assignment_submit_student.objects.filter(assignment=assignment).exists()
    if not cheak_data:
        messages.error(request,'first you submit your data')
        return redirect('student_assignment_list')
    else:
        if request.method == 'POST':
            fm = Assignment_upload_student_form(request.POST,request.FILES,instance= Assignment_submit_student.objects.get(assignment = assignment,student = Student.objects.get(admin = request.user)))
            if fm.is_valid():
                fm.save()
                messages.success(request,'Data changed successful..')

    
    data = {
        'fm':fm
    }
    return render(request,'student/assignment_edit.html',data)

def assignment_result(request):
    result = Assignment_result.objects.filter(assignment__in = Assignment_submit_student.objects.filter(student = Student.objects.get(admin = request.user)))
    data = {
        'data':result
    }
    return render(request,'student/assignment_result.html',data)