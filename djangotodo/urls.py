from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.todos),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.signup),
    path('deleteTodo/',views.deleteTodo),
]
