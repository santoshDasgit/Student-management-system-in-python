
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from server.Email_login import  EmailBackend
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages

from server.models import User,Blog,Blog_comment,Hostel,Transport,Branch,Course,Teacher,Student
from server.forms import Blog_form,Teacher_profile_form,Student_profile_form
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import PasswordChangeForm

def log_in(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
                return redirect('hod_dashboard')
        elif request.user.user_type == '2':
                return redirect('teacher_home')
        elif request.user.user_type == '3':
                return redirect('student_home')
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        user_authenticate_check =authenticate(request,username=username,password=password)

        if user_authenticate_check is not None:
            login(request,user_authenticate_check)

            if user_authenticate_check.user_type == '1':
                return redirect('hod_dashboard')
            elif user_authenticate_check.user_type == '2':
                return redirect('teacher_home')
            elif user_authenticate_check.user_type == '3':
                return redirect('student_home')
        else:
            messages.error(request,'Please enter the correct user and password . Note that both fields may be case-sensitive.')


    return render(request,'login.html')

login_required(login_url='/')
def log_out(request):
    logout(request)
    return redirect('log_in')

login_required(login_url='/')
def profile_update(request):
    fm = ''
    user_type = request.user.user_type
    if user_type == '2':
        fm = Teacher_profile_form(instance=Teacher.objects.get(admin = request.user))
    if user_type == '3':
        fm = Student_profile_form(instance=Student.objects.get(admin = request.user))
    if request.method == 'POST':
        image = request.FILES.get('profile_image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        if user_type == '2':
            fm = Teacher.objects.get(admin = request.user)
            fm.address = request.POST.get('address')
            fm.gender = request.POST.get('gender')
            fm.course = Course.objects.get(id = request.POST.get('course'))
            fm.branch = Branch.objects.get(id = request.POST.get('branch'))
            fm.ph = request.POST.get('ph')
            fm.dob = request.POST.get('dob')
            fm.qualification = request.POST.get('qualification')
            fm.experience = request.POST.get('experience')
            fm.save()
        if user_type == '3':
            fm = Student.objects.get(admin = request.user)
            fm.address = request.POST.get('address')
            fm.gender = request.POST.get('gender')
            fm.ph = request.POST.get('ph')
            fm.dob = request.POST.get('dob')
            fm.father = request.POST.get('father')
            fm.mother = request.POST.get('mother')
            fm.mother_ph = request.POST.get('mother_ph')
            fm.father_ph = request.POST.get('father_ph')
            fm.save()
        try:
            update_user = User.objects.get(id = request.user.id)
            update_user.first_name = first_name
            update_user.last_name = last_name
            update_user.email = email
            update_user.profile_image = image
            if image is None or image is "":
                update_user.profile_image = request.user.profile_image
            update_user.save()
            messages.success(request,'update successfully please <b>Thanks You.!</b>')
            return redirect('profile_update')
        except:
            messages.error(request,'Something error <b>Try again.!</b>')
            
           
    return render(request,'profile_update.html',{'user':request.user,'fm':fm})

def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password change successfully')
            update_session_auth_hash(request,form.user)
    content = {'form': form} 
    return render(request, 'reset_password.html', content)
 
@login_required(login_url='/')
def blog_add(request):
     fm = Blog_form()

     if request.method == 'POST':
          fm = Blog_form(request.POST,request.FILES)
          if fm.is_valid():
               fm.instance.user = request.user
               fm.save()
               messages.success(request,'Blog add successful')
          else:
               messages.error(request,'something error try again')

     data = {
      'fm':fm    
     }
     return render(request,'blog-add.html',data)
@login_required(login_url='/')
def blog(request):
     blog_data = ''
     if request.method == 'POST':
          filters = request.POST.get('filter')
          if filters == 'student':
                allPost = User.objects.filter(user_type = "3")
                blog_data = Blog.objects.filter(user__in=allPost)
          elif filters == 'teacher':
                allPost = User.objects.filter(user_type = "2")
                blog_data = Blog.objects.filter(user__in=allPost)
          elif filters == 'my':
                
                blog_data = Blog.objects.filter(user=request.user)
          else:
               blog_data = Blog.objects.all().order_by('-id')
     else:
          blog_data = Blog.objects.all().order_by('-id')

     data = {
          'data':blog_data
     }
     return render(request,'blog.html',data)
@login_required(login_url='/')
def blog_view(request,url):
    
     if request.method == 'POST':
        msg = request.POST.get('comment')
      
        blog_comments =  Blog_comment(
               blog = Blog.objects.get(id = url),
               user = request.user,
               comment = msg
          )
        blog_comments.save()
     data = {
          'data': Blog.objects.get(id = url),
          'comment':Blog_comment.objects.filter(blog = Blog.objects.get(id = url)).order_by('-id')
     } 
     return render(request,'blog_view.html',data)

@login_required(login_url='/')
def remove_blog_comment(request,url):
     Blog_comment.objects.get(id = url).delete()
     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/')
def remove_blog(request,url):
     Blog.objects.get(id = url).delete()
     return redirect('blog')

@login_required(login_url='/')
def edit_blog(request,url):
     data = Blog.objects.get(id = url)
     fm = Blog_form(instance=data)
     if request.method == 'POST':
        fm = Blog_form(request.POST,request.FILES,instance=data)
        fm.save()
        messages.success(request,'Blog changed successfully ')

      
     data = {
          'fm':fm
     }
     return render(request,'blog_edit.html',data)



@login_required(login_url='/')
def hostel_room(request):
    data = {
        'data':Hostel.objects.all().order_by('-id')
    }
    return render(request,'hostel_room.html',data)

@login_required(login_url='/')
def transport_list(request):
    data = {
        'data':Transport.objects.all().order_by('-id')
    }
    return render(request,'transport_list.html',data)

@login_required(login_url='/')
def branch_list(request):
    return render(request,'branch.html',{'data':Branch.objects.all()})

@login_required(login_url='/')
def course_list(request):
    return render(request,'course.html',{'data':Course.objects.all()})

