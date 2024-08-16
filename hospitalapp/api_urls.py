from django.urls import path

from hospitalapp import views, userviews, doctorviews, adminviews

urlpatterns = [
    # signup
    path("user_signup", userviews.user_signup, name="user_signup"),
    path("doctor_signup", doctorviews.doctor_signup, name="doctor_signup"),
    # login
    path("user_login", views.user_login, name="user_login"),
    path("doctor_login", views.doctor_login, name="doctor_login"),
    # notification
    path("Notificationdetails", adminviews.Notificationdetails, name="Notificationdetails"),
    path("Notificationdelete/<int:pk>/", adminviews.Notificationdelete, name="Notificationdelete"),
    # view doctors
    path("doctordetails", adminviews.doctordetails, name="doctordetails"),
    path("doctordetailsget/<int:pk>/", adminviews.doctordetailsget, name="doctordetailsget"),
    path("doctordetailsdelete/<int:pk>/", adminviews.doctordetailsdelete, name="doctordetailsdelete"),
    # add to list
    path("admindoctoradd", adminviews.admindoctoradd, name="admindoctoradd"),
    #  schedule
    path("doctorscheduleadd", doctorviews.doctorscheduleadd, name="doctorscheduleadd"),
    path("userdoctorprofileget/<int:pk>/", userviews.userdoctorprofileget, name="userdoctorprofileget"),

    path("doctorscheduleget/<int:pk>/", doctorviews.doctorscheduleget, name="doctorscheduleget"),
    path("docscheduledelete/<int:pk>/", doctorviews.docscheduledelete, name="docscheduledelete"),
    # userbooking
    path("userbook/<int:pk>/", userviews.userbook, name="userbook"),
    path("userscheduleget/<int:pk>/", userviews.userscheduleget, name="userscheduleget"),
    path("doctorschedulestatus/<int:pk>/", doctorviews.doctorschedulestatus, name="doctorschedulestatus"),
    path("doctorscheduleview/<int:pk>/", doctorviews.doctorscheduleview, name="doctorscheduleview"),
    # search
    path("usersearch", userviews.usersearch, name="usersearch"),
    # account delete
    path("docaccountdelete/<int:pk>/", doctorviews.docaccountdelete, name="docaccountdelete"),
    path("useraccountdelete/<int:pk>/", userviews.useraccountdelete, name="useraccountdelete"),
    # user schedule view
    path("userschedulestatus/<int:pk>/", userviews.userschedulestatus, name="userschedulestatus"),
    path("userscheduleview/<int:pk>/", userviews.userscheduleview, name="userscheduleview"),
    # doctor profile update
    path("docprofileupdate/<int:pk>/",doctorviews.docprofileupdate,name="docprofileupdate"),
    path("docChangePassword/<int:pk>/",doctorviews.docChangePassword,name="docChangePassword")
]
