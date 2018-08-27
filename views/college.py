from django.shortcuts import *
from django.shortcuts import get_object_or_404
from onlineapp.forms.allforms import *
from django.views.generic import *
from django.urls import *
from onlineapp.forms.auth import *
from django.contrib.auth.forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import *

app_name="templates"

class collegeView(LoginRequiredMixin,View):
    # def get_context_data(self,**kwargs):
    #     context=support()
    login_url = 'onlineapp:login'


    def get(self,request,*args,**kwargs):
        #ipdb.set_trace()
        colleges=College.objects.all()
        context = {
            'jails': colleges
        }
        context.update({'userpermissions':self.request.user.get_all_permissions()})
        return render(request,
                     template_name='onlineapp/collegeList.html',
                      context=context
                      )
class collegeDetailView(LoginRequiredMixin,DetailView):
    login_url = 'onlineapp:login'
    model=College
    template_name = 'onlineapp/college_detail.html'
    def get_object(self, queryset=None):

        return get_object_or_404(College,**self.kwargs)
    def get_context_data(self, **kwargs):
        context=super(collegeDetailView,self).get_context_data(**kwargs)
        college=context.get('college')
        students=list(college.student_set.order_by('email'))
        # context.update({
        #      'jail':students
        # })
        context['jail']=students
        context['collegeid']=college.id

        return context



class CreateCollegeView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'onlineapp:login'
    permission_required = "onlineapp.add_college"
    permission_denied_message = "User des not have permission to create a college"
    raise_exception = True
    model = College
    template_name = 'onlineapp/college_form.html'
    form_class =addCollege
    success_url = reverse_lazy('onlineapp:displayCollege')

class updateCollegeView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = 'onlineapp:login'
    permission_required = "onlineapp.change_college"
    permission_denied_message = "User des not have permission to create a college"
    raise_exception = True
    model = College
    template_name = 'onlineapp/college_form.html'
    form_class =addCollege
    success_url = reverse_lazy('onlineapp:displayCollege')
    def get_object(self, queryset=None):

        return get_object_or_404(College,**self.kwargs)
    def get_context_data(self, **kwargs):
        context=super(updateCollegeView,self).get_context_data(**kwargs)

        return context



class createStudentView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.add_student'
    model = Student
    form_class = addStudent
    #template_name = 'student_form.html'

    def get_context_data(self, **kwargs):
        context = super(createStudentView, self).get_context_data(**kwargs)
        test_form = addMockTest
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('pk'))
        student_form = addStudent(request.POST)
        test_form = addMockTest(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()

            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()
            else:
                return redirect('login')
        return redirect('onlineapp:college_list',college.id)




class updateStudentView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.change_student'
    model = Student
    form_class = addStudent
    #template_name = 'student_form.html'

    def get_context_data(self, **kwargs):
        context = super(updateStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')
        test_form = addMockTest(instance=student_form.mocktest1)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = addStudent(request.POST, instance=student)
        test_form = addMockTest(request.POST, instance=student.mocktest1)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())
        form.save()
        test_form.save()
        return redirect('onlineapp:college_list',kwargs.get('cid'))



class deleteCollegeView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.delete_college'
    model = College
    template_name = 'onlineapp/delete_confirmation.html'
    success_url = reverse_lazy('onlineapp:displayCollege')

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)


class deleteStudentView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.delete_student'
    model=Student
    template_name = 'onlineapp/delete_confirmation.html'
    success_url=reverse_lazy('onlineapp:displayCollege')
    def get_object(self, queryset=None):
        self.id=self.kwargs['pk']
        return get_object_or_404(Student, **self.kwargs)



class studentView(LoginRequiredMixin,View):
    login_url = 'onlineapp:login'
    def get(self,request,*args,**kwargs):
        student=Student.objects.all()
        return render(request,template_name='studentList.html',context={'studentData':student})


class loginView(View):
    def get(self,request):
        form=loginForm
        return render(request,'onlineapp/login.html',{'form':form})
    def post(self,request):
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('onlineapp:displayCollege')
            else:
                return redirect('onlineapp:login')



class signupView(View):
    def get(self,request):
        requiredForm=signUp()
        template='onlineapp/signup.html'
        return render(request,template_name=template,context={'form':requiredForm})
    def post(self,request):
        form=signUp(request.POST)
        if(form.is_valid()):
            user=User.objects.create_user(**form.cleaned_data)
            authenticate(user,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            return redirect('onlineapp:displayCollege')





def logout_user(request):
    logout(request)
    return redirect('onlineapp:login')