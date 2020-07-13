from django.conf.urls import url, include

from friends import views

urlpatterns = [
    url(r'^show/all$', views.FriendsView.as_view()),
    url(r'^add$', views.FriendsAdd.as_view()),
]