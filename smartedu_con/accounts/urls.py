from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginView,name='login'),
    path('register/',views.registerView,name='register'),
    path('logout/',views.logoutView,name='logout'),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('enroll_the_course/',views.enroll_the_course,name='enroll_the_course'),
    path('release_the_course/',views.release_the_course,name='release_the_course'),
]
