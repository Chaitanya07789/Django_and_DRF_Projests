from django.urls import path
from todo.views import *

urlpatterns = [
    path('',signup),
    path('login/',loginn),
    path('todo/',todo),
    path('edit_todo/<int:id>',edit_todo,name='edit_todo'),
    path('delete_todo/<int:id>',delete_todo),
    path('signout/',signout,name='signout'),
    
]