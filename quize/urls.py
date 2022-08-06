from django.urls import path
from .models import *
from .views import *


app_name = "quize"

urlpatterns = [

path('question/', create_questions.as_view(), name='question'),
path('answer/', create_answers.as_view(), name='answer'),
path('', relations.as_view(), name='relation'),

]
