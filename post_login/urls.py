from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.quiz , name="quiz"),
    url(r'^question.html$', views.question , name="question"),
    url(r'^ques1.html$', views.ques1 , name="ques1"),
    # url(r'^registration.html', views.register, name="registration"),
]