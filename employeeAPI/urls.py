from django.conf.urls import url, include

from employeeAPI import views

urlpatterns = [
    url(r'^show/all$', views.EmployeeAll.as_view()),
    url(r'^create', views.EmployeeProcess.as_view()),
    url(r'^update', views.EmployeeUpdate.as_view()),
    url(r'^delete', views.EmployeeUpdate.as_view()),
]