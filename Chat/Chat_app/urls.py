from django.urls import path
from .views import loginview, register, chat_body, logoutview, history #, message_add

urlpatterns=[
    path('login/', loginview.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('logout/', logoutview.as_view(), name='logout'),
    path('body/', chat_body.as_view() , name='body'),
    path('history/', history.as_view(), name='history'),
]