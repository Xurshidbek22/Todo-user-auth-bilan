
from django.contrib import admin
from django.urls import path
from new.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo),
    path('register/', register),
    path('todo_ochir/<int:son>/', todoni_ochir),
    path('todo_edit/<int:son>/', todoni_tahrirlash),
    path('', loginView),

    path('logout/', logoutView),
]
