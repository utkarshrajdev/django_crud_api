from django.urls import path
from .views import Signup,Login

urlpatterns = [
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
]