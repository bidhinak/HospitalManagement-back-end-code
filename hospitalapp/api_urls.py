from django.urls import path

from hospitalapp import views, userviews, doctorviews, adminviews

urlpatterns=[
    # signup
    path("user_signup",userviews.user_signup,name="user_signup"),
    path("doctor_signup", doctorviews.doctor_signup, name="doctor_signup"),
    # login
    path("user_login",views.user_login,name="user_login"),
    path("doctor_login", views.doctor_login, name="doctor_login"),
    # notification
    path("Notificationdetails",adminviews.Notificationdetails,name="Notificationdetails"),
    # view doctors
    path("doctordetails", adminviews.doctordetails, name="doctordetails"),
    path("doctordetailsget/<int:pk>/", adminviews.doctordetailsget, name="doctordetailsget"),
    # add to list
    path("admindoctoradd",adminviews.admindoctoradd,name="admindoctoradd"),
    # schedule
    path("doctorscheduleadd",doctorviews.doctorscheduleadd,name="doctorscheduleadd"),
    path("home",userviews.home,name="home"),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path("new",views.new, name="new"),

]