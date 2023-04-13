from django.urls import path
from .views import loginview, register, chat_body, logoutview
urlpatterns=[
    path('login/', loginview.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('logout/', logoutview.as_view(), name='logout'),
    path('body/', chat_body.as_view(), name='body'),
]