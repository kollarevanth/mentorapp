from django.contrib import admin
from django.urls import path
from onlineapp import views
from django.conf.urls import include, url
from django.conf import settings
from views.college import *
from views.collegeserialViews import *
from views.studentSerialViews import *
from views import *
import debug_toolbar

app_name='onlineapp'

urlpatterns = [
 #   path('admin/', admin.site.urls),
    path('details/<int:value>',views.print_student_details_acronym),
    path('count/',views.test_http_request),
    path('exception',views.test_exception),
    path('colleges/',collegeView.as_view(),name='displayCollege'),
    path('collegeDetailView/<int:pk>/',collegeDetailView.as_view(),name='college_list'),
    path('createCollegeView/', CreateCollegeView.as_view(), name='add_colleges'),
    path('addStudent/<int:pk>',createStudentView.as_view(),name='add_student'),
    path('colleges/<int:pk>',updateCollegeView.as_view(),name="update_college"),
    path('colleges/deleteCollege/<int:pk>',deleteCollegeView.as_view(),name="deleteCollege"),
    path('updateStudent/<int:cid>/<int:pk>',updateStudentView.as_view(),name="updateStudent"),
    path('deleteStudent/<int:pk>',deleteStudentView.as_view(),name="deleteStudent"),
    path('signup/',signupView.as_view(),name="signUp"),
    path('',loginView.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('serialize/',collegeListApi.as_view(),name='serialData'),
    path('createSerialize/',createCollegeSerializer.as_view(),name='createSerialize'),
    path('updateSerialize/<str:name>',updateCollegeSerializer.as_view(),name='updateSerialize'),
    path('deleteSerialize/<str:name>',deleteCollegeSerializer.as_view(),name='deleteSerialize'),
    path('functionSerializer/college_list',college_list),
    path('functionSerializer/college_detail/<int:pk>',college_detail),
    path('studentserialize/<int:college__id>',studentListApi.as_view(),name='studentLsitSerialize'),
    path('studentDetail/<int:college__id>/<int:student__id>',studentDetailsApi.as_view(),name='studentDetailsSerialize'),
    path('studentDetailDelete/<int:college__id>/<int:pk>', studentDetailDeleteApi.as_view(),name='studentDetailDeleteSerialize'),
    path('studentDetailUpdate/<int:college__id>/<int:pk>', studentDetailsUpdateApi.as_view(),name='studentDetailUpdateSerialize'),
    path('studentDetailCreate/<int:college__id>', studentDetailCreateApi.as_view(),name='studentDetailsCreateSerialize'),
    path('fstudentlist/',student_list),

    path('fstudentdetail/<int:pk>',student_detail)


]
