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
    # view users
    path("userdetails",adminviews.userdetails,name="userdetails"),
    path("userdetailsdelete/<int:pk>/",adminviews.userdetailsdelete,name="userdetailsdelete"),
    # view user bookings
    path("userbookingsget/<int:pk>/",adminviews.userbookingsget,name="userbookingsget"),
    path("userbookingview/<int:pk>/",adminviews.userbookingview,name="userbookingview"),
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
    path("userbookget",userviews.userbookget,name="userbookget"),
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
    path("docprofileupdate2/<int:pk>/",doctorviews.docprofileupdate2,name="docprofileupdate2"),
    path("docChangePassword/<int:pk>/",doctorviews.docChangePassword,name="docChangePassword"),
    path("docprofilephotoupdate/<int:pk>/",doctorviews.docprofilephotoupdate,name="docprofilephotoupdate"),
    path("docprofilephotoupdate2/<int:pk>/", doctorviews.docprofilephotoupdate2, name="docprofilephotoupdate2"),
    # user profile update
    path("userChangePassword/<int:pk>/",userviews.userChangePassword,name="userChangePassword"),
    path("userprofileupdate/<int:pk>/",userviews.userprofileupdate,name="userprofileupdate"),
    # docreport
    path("docreportadd/<int:pk>/",doctorviews.docreportadd,name="docreportadd"),
    path("docreportget/<int:pk>/",doctorviews.docreportget,name="docreportget"),
]
