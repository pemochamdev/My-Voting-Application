from django.urls import path
from django.contrib.auth.views import LoginView
from voteapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<slug>/', views.detail, name='detail'),
    path('vote/result/<slug>/', views.result, name='result'),
    #path('signin/', views.signin, name='signin'),

    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='logout'),
    #path('signin/', LoginView.as_view(template_name = 'signin.html'), name='signin'),
    path('signin/', views.CoustomLoginView.as_view(), name='signin'),

    
]
