from django.urls import path

from .views import *

urlpatterns = [
    path('Tests/', tests_1, name='test_1'),
    path('LogIn/', user_login, name='login'),
    path('', users, name="todo"),
    path('Test/', t, name='t'),
    path('Test2/', t2, name='t2'),
    path('Test3/', t3, name='t3'),
    path('Test4/', t4, name='t4'),
    path('Test5/', t5, name='t5'),
    path('Test6/', t6, name='t6'),
    path('Exit/', ex, name='ex'),
    path('Answer_sheet/', test_ansver, name='test_answer')
]
